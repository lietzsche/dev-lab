"""터널 프로필 목록의 저장/불러오기.

비밀번호나 키 암호문은 이 파일에 절대 포함되지 않는다. 오직 프로필의
연결 정보(호스트/포트/사용자 이름/키 경로 등)만 JSON으로 직렬화된다.
"""
from __future__ import annotations

import json
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class AuthKind:
    """인증 방식. ``kind``는 "password" 또는 "private_key"."""

    kind: str = "password"
    key_path: str = ""

    @staticmethod
    def password() -> "AuthKind":
        return AuthKind(kind="password")

    @staticmethod
    def private_key(key_path: str) -> "AuthKind":
        return AuthKind(kind="private_key", key_path=key_path)

    @property
    def is_private_key(self) -> bool:
        return self.kind == "private_key"


@dataclass
class TunnelProfile:
    name: str
    ssh_host: str
    username: str
    ssh_port: int = 22
    auth: AuthKind = field(default_factory=AuthKind.password)
    local_bind: str = "127.0.0.1"
    local_port: int = 8080
    remote_host: str = "127.0.0.1"
    remote_port: int = 80
    auto_start: bool = False
    trust_on_first_use: bool = True
    id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "TunnelProfile":
        auth_data = data.get("auth") or {}
        return TunnelProfile(
            id=data.get("id") or uuid.uuid4().hex,
            name=data.get("name", "새 터널"),
            ssh_host=data.get("ssh_host", ""),
            ssh_port=int(data.get("ssh_port", 22)),
            username=data.get("username", ""),
            auth=AuthKind(
                kind=auth_data.get("kind", "password"),
                key_path=auth_data.get("key_path", ""),
            ),
            local_bind=data.get("local_bind", "127.0.0.1"),
            local_port=int(data.get("local_port", 8080)),
            remote_host=data.get("remote_host", "127.0.0.1"),
            remote_port=int(data.get("remote_port", 80)),
            auto_start=bool(data.get("auto_start", False)),
            trust_on_first_use=bool(data.get("trust_on_first_use", True)),
        )


@dataclass
class AppConfig:
    profiles: list[TunnelProfile] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {"profiles": [p.to_dict() for p in self.profiles]}

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "AppConfig":
        return AppConfig(profiles=[TunnelProfile.from_dict(p) for p in data.get("profiles", [])])


def config_dir() -> Path:
    """OS별 표준 설정 디렉터리 (러스트판 PortKeeper와 충돌하지 않도록 별도 이름 사용)."""
    import os
    import sys

    if sys.platform == "win32":
        base = os.environ.get("APPDATA") or str(Path.home() / "AppData" / "Roaming")
        return Path(base) / "PortKeeperPy"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "PortKeeperPy"
    xdg = os.environ.get("XDG_CONFIG_HOME") or str(Path.home() / ".config")
    return Path(xdg) / "portkeeper-py"


def config_path() -> Path:
    return config_dir() / "config.json"


def known_hosts_path() -> Path:
    return config_dir() / "known_hosts"


def load() -> AppConfig:
    path = config_path()
    if not path.exists():
        return AppConfig()
    with path.open("r", encoding="utf-8") as f:
        return AppConfig.from_dict(json.load(f))


def save(config: AppConfig) -> None:
    directory = config_dir()
    directory.mkdir(parents=True, exist_ok=True)
    with config_path().open("w", encoding="utf-8") as f:
        json.dump(config.to_dict(), f, ensure_ascii=False, indent=2)
