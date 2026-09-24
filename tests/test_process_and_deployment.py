"""Public behavior tests for P10-4 process and deployment boundaries."""

import uvicorn
from fastapi.testclient import TestClient

from knowledge_lab.lessons.p10_4_process_and_deployment import (
    build_server_config,
    health_app,
    health_state,
    liveness_status,
    readiness_status,
    run_server_lifecycle,
    build_container_command,
)
import pytest


def test_server_lifecycle_starts_and_stops_in_current_process() -> None:
    config = build_server_config()
    config.load()
    server = uvicorn.Server(config)

    started, stopped = run_server_lifecycle(server)

    assert started is True
    assert server.should_exit is True
    assert stopped is True


def test_liveness_and_readiness_have_different_state_meanings() -> None:
    assert liveness_status() == (200, "alive")
    assert readiness_status(False) == (503, "not ready")
    assert readiness_status(True) == (200, "ready")


def test_health_endpoints_follow_application_lifespan() -> None:
    assert health_state["ready"] is False

    client_without_lifespan = TestClient(health_app)
    try:
        response = client_without_lifespan.get("/health/ready")
        assert response.status_code == 503
        assert response.json() == {"status": "not ready"}
    finally:
        client_without_lifespan.close()

    with TestClient(health_app) as client:
        assert health_state["ready"] is True
        live_response = client.get("/health/live")
        ready_response = client.get("/health/ready")
        assert live_response.status_code == 200
        assert live_response.json() == {"status": "alive"}
        assert ready_response.status_code == 200
        assert ready_response.json() == {"status": "ready"}

    assert health_state["ready"] is False


def test_build_container_command_validates_and_formats_cli_arguments() -> None:
    cmd = build_container_command(
        app_target="my_module:app",
        host="0.0.0.0",
        port=8080,
        workers=2,
    )
    assert cmd == [
        "uvicorn",
        "my_module:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8080",
        "--workers",
        "2",
    ]

    with pytest.raises(ValueError, match="invalid port"):
        build_container_command(port=0)

    with pytest.raises(ValueError, match="invalid port"):
        build_container_command(port=70000)

    with pytest.raises(ValueError, match="workers must be >= 1"):
        build_container_command(workers=0)
