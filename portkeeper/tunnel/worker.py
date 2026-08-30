"""하나의 터널 프로필을 감독하는 백그라운드 스레드.

연결이 끊기면 지수 백오프(1초 -> 2초 -> ... 최대 30초)를 두고 자동으로
재연결한다. 로컬 TCP 리스너가 수락한 각 연결마다 SSH 위에 direct-tcpip
채널을 새로 열고, 두 개의 중계 스레드로 데이터를 그대로 흘려보낸다
(표준 ``ssh -L`` 과 동일한 동작).
"""
from __future__ import annotations

import queue
import socket
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union

import paramiko

from ..config import TunnelProfile
from .handler import TofuPolicy

MIN_BACKOFF = 1.0
MAX_BACKOFF = 30.0
HEARTBEAT_SECONDS = 2.0
ACCEPT_POLL_SECONDS = 1.0


@dataclass(frozen=True)
class PasswordCredentials:
    password: str


@dataclass(frozen=True)
class PrivateKeyCredentials:
    key_path: str
    passphrase: Optional[str] = None


Credentials = Union[PasswordCredentials, PrivateKeyCredentials]


class StatusEvent:
    """GUI 스레드로 보내는 상태 갱신 메시지. ``kind`` 로 분기한다."""

    def __init__(self, kind: str, **fields: object) -> None:
        self.kind = kind
        self.fields = fields


class _ConnectionCounter:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._value = 0

    def increment(self) -> None:
        with self._lock:
            self._value += 1

    def decrement(self) -> None:
        with self._lock:
            self._value -= 1

    @property
    def value(self) -> int:
        with self._lock:
            return self._value


def run(
    profile: TunnelProfile,
    credentials: Credentials,
    known_hosts_path: Path,
    stop_event: threading.Event,
    status_queue: "queue.Queue[StatusEvent]",
    log_queue: "queue.Queue[str]",
) -> None:
    """감독 루프. ``stop_event`` 가 설정되면 재연결을 멈추고 스레드를 종료한다."""

    attempt = 0
    backoff = MIN_BACKOFF

    while not stop_event.is_set():
        attempt += 1
        status_queue.put(StatusEvent("connecting"))
        log_queue.put(f"[{profile.name}] 연결을 시도합니다 ({attempt}번째 시도)")

        try:
            _connect_and_serve(profile, credentials, known_hosts_path, stop_event, status_queue, log_queue)
            backoff = MIN_BACKOFF
        except Exception as exc:  # noqa: BLE001 - 재연결 루프에서는 모든 예외를 잡아 기록한다
            message = str(exc) or exc.__class__.__name__
            log_queue.put(f"[{profile.name}] 연결 종료: {message}")
            status_queue.put(StatusEvent("error", message=message))

        if stop_event.is_set():
            break

        status_queue.put(StatusEvent("reconnecting", attempt=attempt, retry_in=backoff))
        stop_event.wait(backoff)
        backoff = min(backoff * 2, MAX_BACKOFF)

    status_queue.put(StatusEvent("stopped"))


def _connect_and_serve(
    profile: TunnelProfile,
    credentials: Credentials,
    known_hosts_path: Path,
    stop_event: threading.Event,
    status_queue: "queue.Queue[StatusEvent]",
    log_queue: "queue.Queue[str]",
) -> None:
    log = lambda msg: log_queue.put(f"[{profile.name}] {msg}")  # noqa: E731

    client = paramiko.SSHClient()
    if known_hosts_path.exists():
        client.load_host_keys(str(known_hosts_path))
    policy = TofuPolicy(profile.trust_on_first_use, log)
    client.set_missing_host_key_policy(policy)

    try:
        if isinstance(credentials, PasswordCredentials):
            client.connect(
                profile.ssh_host,
                port=profile.ssh_port,
                username=profile.username,
                password=credentials.password,
                look_for_keys=False,
                allow_agent=False,
                timeout=10,
                banner_timeout=10,
                auth_timeout=15,
            )
        else:
            client.connect(
                profile.ssh_host,
                port=profile.ssh_port,
                username=profile.username,
                key_filename=credentials.key_path,
                passphrase=credentials.passphrase,
                look_for_keys=False,
                allow_agent=False,
                timeout=10,
                banner_timeout=10,
                auth_timeout=15,
            )
    except paramiko.BadHostKeyException as exc:
        raise RuntimeError(
            f"저장된 호스트 키가 서버 키와 다릅니다! 중간자 공격 가능성이 있어 연결을 중단합니다 ({exc})"
        ) from exc
    except paramiko.AuthenticationException as exc:
        raise RuntimeError("인증에 실패했습니다 (사용자 이름 / 비밀번호 / 키를 확인하세요)") from exc

    if policy.learned:
        known_hosts_path.parent.mkdir(parents=True, exist_ok=True)
        client.save_host_keys(str(known_hosts_path))

    log("SSH 인증에 성공했습니다")

    transport = client.get_transport()
    assert transport is not None
    transport.set_keepalive(15)

    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        listener.bind((profile.local_bind, profile.local_port))
    except OSError as exc:
        client.close()
        raise RuntimeError(f"로컬 포트를 열 수 없습니다 ({profile.local_bind}:{profile.local_port}): {exc}") from exc
    listener.listen(16)
    listener.settimeout(ACCEPT_POLL_SECONDS)

    log(f"로컬 {profile.local_bind}:{profile.local_port} 에서 연결을 대기합니다")

    since = time.monotonic()
    active = _ConnectionCounter()
    status_queue.put(StatusEvent("connected", since=since, active_connections=0))

    try:
        last_heartbeat = time.monotonic()
        while not stop_event.is_set():
            if not transport.is_active():
                raise RuntimeError("SSH 세션이 종료되었습니다 (keepalive 응답 없음)")

            try:
                client_sock, addr = listener.accept()
            except socket.timeout:
                now = time.monotonic()
                if now - last_heartbeat >= HEARTBEAT_SECONDS:
                    status_queue.put(
                        StatusEvent("connected", since=since, active_connections=active.value)
                    )
                    last_heartbeat = now
                continue

            active.increment()
            threading.Thread(
                target=_handle_connection,
                args=(client_sock, transport, profile, addr, active, log_queue),
                daemon=True,
            ).start()
    finally:
        listener.close()
        client.close()


def _handle_connection(
    client_sock: socket.socket,
    transport: paramiko.Transport,
    profile: TunnelProfile,
    addr: tuple,
    active: _ConnectionCounter,
    log_queue: "queue.Queue[str]",
) -> None:
    try:
        channel = transport.open_channel(
            "direct-tcpip",
            dest_addr=(profile.remote_host, profile.remote_port),
            src_addr=addr,
            timeout=10,
        )
    except Exception as exc:  # noqa: BLE001
        log_queue.put(f"[{profile.name}] 채널을 열 수 없습니다: {exc}")
        client_sock.close()
        active.decrement()
        return

    t1 = threading.Thread(target=_pump, args=(client_sock, channel), daemon=True)
    t2 = threading.Thread(target=_pump, args=(channel, client_sock), daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    for closable in (channel, client_sock):
        try:
            closable.close()
        except OSError:
            pass
    active.decrement()


def _pump(src, dst) -> None:
    try:
        while True:
            data = src.recv(4096)
            if not data:
                break
            dst.sendall(data)
    except OSError:
        pass
    finally:
        try:
            dst.shutdown(socket.SHUT_WR)
        except OSError:
            pass
