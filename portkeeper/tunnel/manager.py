"""실행 중인 터널들을 프로필 id로 추적하는 감독자.

실제 연결/포워딩은 ``worker.run`` 이 담당하는 백그라운드 스레드에서
수행되고, 이 클래스는 그 스레드와 최신 상태 큐를 보관하는 얇은 레지스트리
역할만 한다.
"""
from __future__ import annotations

import queue
import threading
from dataclasses import dataclass
from pathlib import Path

from ..config import TunnelProfile
from . import worker
from .worker import Credentials, StatusEvent


@dataclass
class _RunningTunnel:
    thread: threading.Thread
    stop_event: threading.Event
    status_queue: "queue.Queue[StatusEvent]"
    log_queue: "queue.Queue[str]"
    last_status: StatusEvent


class TunnelManager:
    def __init__(self) -> None:
        self._running: dict[str, _RunningTunnel] = {}

    def is_running(self, profile_id: str) -> bool:
        return profile_id in self._running

    def status(self, profile_id: str) -> StatusEvent:
        tunnel = self._running.get(profile_id)
        if tunnel is None:
            return StatusEvent("stopped")
        return tunnel.last_status

    def start(
        self,
        profile: TunnelProfile,
        credentials: Credentials,
        known_hosts_path: Path,
        log_queue: "queue.Queue[str]",
    ) -> None:
        if profile.id in self._running:
            return

        stop_event = threading.Event()
        status_queue: "queue.Queue[StatusEvent]" = queue.Queue()
        thread = threading.Thread(
            target=worker.run,
            args=(profile, credentials, known_hosts_path, stop_event, status_queue, log_queue),
            daemon=True,
        )
        self._running[profile.id] = _RunningTunnel(
            thread=thread,
            stop_event=stop_event,
            status_queue=status_queue,
            log_queue=log_queue,
            last_status=StatusEvent("connecting"),
        )
        thread.start()

    def stop(self, profile_id: str) -> None:
        tunnel = self._running.pop(profile_id, None)
        if tunnel is not None:
            tunnel.stop_event.set()

    def stop_all(self) -> None:
        for profile_id in list(self._running.keys()):
            self.stop(profile_id)

    def poll(self) -> None:
        """모든 실행 중인 터널의 상태 큐를 비워 최신 상태를 반영한다.

        매 프레임 GUI 루프에서 호출한다.
        """
        for tunnel in self._running.values():
            while True:
                try:
                    tunnel.last_status = tunnel.status_queue.get_nowait()
                except queue.Empty:
                    break
