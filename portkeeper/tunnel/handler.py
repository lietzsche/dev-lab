"""SSH 호스트 키 검증 정책 (TOFU: Trust On First Use).

이미 known_hosts 파일에 등록된 호스트인데 서버가 다른 키를 보내면
paramiko가 ``BadHostKeyException``을 자동으로 발생시킨다 (중간자 공격 방어).
등록되지 않은 새 호스트를 만났을 때만 이 정책의 ``missing_host_key``가
호출되며, 여기서 신뢰 여부를 결정한다.
"""
from __future__ import annotations

from collections.abc import Callable

import paramiko


class TofuPolicy(paramiko.MissingHostKeyPolicy):
    def __init__(self, trust_on_first_use: bool, log: Callable[[str], None]) -> None:
        self.trust_on_first_use = trust_on_first_use
        self.log = log
        self.learned = False

    def missing_host_key(self, client: paramiko.SSHClient, hostname: str, key: paramiko.PKey) -> None:
        if not self.trust_on_first_use:
            self.log(f"알 수 없는 호스트 키이며 TOFU가 꺼져 있어 연결을 거부합니다: {hostname}")
            raise paramiko.SSHException(f"{hostname}: 등록되지 않은 호스트 키 (TOFU 비활성화)")

        client.get_host_keys().add(hostname, key.get_name(), key)
        self.learned = True
        self.log(f"새 호스트 키를 신뢰 목록에 등록했습니다 (지문: {key.fingerprint})")
