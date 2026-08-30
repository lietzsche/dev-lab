from pathlib import Path

from portkeeper import config
from portkeeper.config import AppConfig, AuthKind, TunnelProfile


def test_password_profile_round_trips_through_dict() -> None:
    profile = TunnelProfile(
        name="사내 DB",
        ssh_host="bastion.example.com",
        username="myuser",
        auth=AuthKind.password(),
        local_port=5432,
        remote_host="10.0.1.5",
        remote_port=5432,
    )

    restored = TunnelProfile.from_dict(profile.to_dict())

    assert restored == profile
    assert restored.auth.kind == "password"
    assert not restored.auth.is_private_key


def test_private_key_profile_round_trips_through_dict() -> None:
    profile = TunnelProfile(
        name="관리 콘솔",
        ssh_host="bastion.example.com",
        username="myuser",
        auth=AuthKind.private_key("/home/me/.ssh/id_ed25519"),
        auto_start=True,
    )

    restored = TunnelProfile.from_dict(profile.to_dict())

    assert restored == profile
    assert restored.auth.is_private_key
    assert restored.auth.key_path == "/home/me/.ssh/id_ed25519"


def test_password_is_never_part_of_the_serialized_shape() -> None:
    profile = TunnelProfile(name="사내 DB", ssh_host="h", username="u")

    data = profile.to_dict()

    assert "password" not in data
    assert "password" not in data["auth"]


def test_save_and_load_round_trip(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(config, "config_dir", lambda: tmp_path)

    original = AppConfig(
        profiles=[
            TunnelProfile(name="A", ssh_host="h1", username="u1"),
            TunnelProfile(name="B", ssh_host="h2", username="u2", auth=AuthKind.private_key("/k")),
        ]
    )
    config.save(original)

    loaded = config.load()

    assert loaded == original
    assert (tmp_path / "config.json").exists()


def test_load_missing_file_returns_empty_config(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(config, "config_dir", lambda: tmp_path)

    loaded = config.load()

    assert loaded == AppConfig()
