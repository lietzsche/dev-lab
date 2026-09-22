"""P10-1: configuration과 secret의 경계를 관찰한다."""

from dataclasses import dataclass, field
import os


@dataclass(frozen=True)
class AppSettings:
    http_port: int
    api_token: str | None = field(repr=False)
    mode: str


def load_settings() -> AppSettings:
    api_token = os.getenv("KNOWLEDGE_LAB_API_TOKEN")
    mode = load_mode()
    if mode == "production" and (api_token is None or api_token == ""):
        raise ValueError("production need the api token")
    return AppSettings(
        http_port=load_http_port(),
        api_token=api_token,
        mode=mode,
    )


def load_http_port() -> int:
    port = int(os.getenv("KNOWLEDGE_LAB_PORT", "8000"))
    if port < 1 or port > 65535:
        raise ValueError(f"{port}: can't use for port")
    return port


def load_mode() -> str:
    DEV = "development"
    mode = os.getenv("KNOWLEDGE_LAB_MODE", DEV)
    if mode not in [DEV, "test", "production"]:
        raise ValueError(f"{mode}: is not mode")
    return mode


def run() -> None:
    """Run the current configuration and secrets exercise."""
    print()
    print("P10-1 configuration과 secret 시작")

    settings = load_settings()
    print(f"settings: {settings}")
    print(f"in settings api_token is not None: {settings.api_token is not None}")
