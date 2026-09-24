"""P10-4: process와 deployment 경계를 관찰한다."""

import os
import socket
import threading
import time
import uvicorn

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient


health_state = {"ready": False}


@asynccontextmanager
async def health_lifespan(_app: FastAPI) -> AsyncIterator[None]:
    health_state["ready"] = True
    try:
        yield
    finally:
        health_state["ready"] = False


def liveness_status() -> tuple[int, str]:
    return 200, "alive"


def readiness_status(application_ready: bool) -> tuple[int, str]:
    if application_ready:
        return 200, "ready"
    return 503, "not ready"


health_app = FastAPI(lifespan=health_lifespan)


@health_app.get("/health/live")
def get_liveness() -> JSONResponse:
    status_code, message = liveness_status()
    return JSONResponse(status_code=status_code, content={"status": message})


@health_app.get("/health/ready")
def get_readiness() -> JSONResponse:
    status_code, message = readiness_status(health_state["ready"])
    return JSONResponse(status_code=status_code, content={"status": message})


def build_server_config() -> uvicorn.Config:
    return uvicorn.Config(
        app="knowledge_lab.lessons.p9_3_fastapi_application:app",
        host="127.0.0.1",
        port=8000,
        workers=1,
    )


def run_server_lifecycle(
    server: uvicorn.Server,
) -> tuple[bool, bool]:
    server_socket = socket.socket()
    server_socket.bind(("127.0.0.1", 0))
    server_socket.listen()
    server_thread = threading.Thread(
        target=server.run,
        kwargs={"sockets": [server_socket]},
        daemon=True,
        name="uvicorn-lifecycle",
    )
    try:
        server_thread.start()
        deadline = time.monotonic() + 2.0
        while not server.started:
            if not server_thread.is_alive():
                raise RuntimeError("server stopped before startup")
            if time.monotonic() >= deadline:
                raise TimeoutError("server startup timed out")
            time.sleep(0.01)
        started = server.started
    finally:
        server.should_exit = True
        server_thread.join(timeout=2.0)
        server_socket.close()
    stopped = not server_thread.is_alive()
    return started, stopped


def build_container_command(
    app_target: str = "knowledge_lab.lessons.p9_3_fastapi_application:app",
    host: str = "0.0.0.0",
    port: int = 8000,
    workers: int = 1,
) -> list[str]:
    if port < 1 or port > 65535:
        raise ValueError("invalid port")
    if workers < 1:
        raise ValueError("workers must be >= 1")
    return [
        "uvicorn",
        app_target,
        "--host",
        host,
        "--port",
        str(port),
        "--workers",
        str(workers),
    ]


def run() -> None:
    """Run the current process and deployment exercise."""
    print()
    print("P10-4 process와 deployment 시작")

    config = build_server_config()
    process_id_before_load = os.getpid()
    print(f"runtime process id: {process_id_before_load}")
    print(f"ASGI app target: {config.app}")
    print(f"server host: {config.host}")
    print(f"server port: {config.port}")
    print(f"worker count: {config.workers}")

    print(f"config loaded before: {config.loaded}")
    config.load()
    print(f"config loaded after: {config.loaded}")
    print(f"config app is string: {isinstance(config.app, str)}")
    print(f"loaded app is callable: {callable(config.loaded_app)}")
    print(f"process id unchanged after load: {process_id_before_load == os.getpid()}")

    server = uvicorn.Server(config)
    print(f"server owns config: {server.config is config}")
    print(f"server started before serve: {server.started}")
    print(f"server should exit before serve: {server.should_exit}")
    print(
        "process id unchanged after server creation: "
        f"{process_id_before_load == os.getpid()}"
    )

    started, stopped = run_server_lifecycle(server)
    print(f"server started during serve: {started}")
    print(f"graceful shutdown requested: {server.should_exit}")
    print(f"server thread stopped: {stopped}")
    print(
        f"process id unchanged after shutdown: {process_id_before_load == os.getpid()}"
    )

    print(f"liveness: {liveness_status()}")
    print(f"readiness before startup: {readiness_status(False)}")
    print(f"readiness after startup: {readiness_status(True)}")
    print(f"readiness during shutdown: {readiness_status(False)}")

    print(f"health ready before client: {health_state['ready']}")

    client_without_lifespan = TestClient(health_app)
    try:
        ready_response_without_lifespan = client_without_lifespan.get("/health/ready")
        print(
            f"readiness before lifespan status: {ready_response_without_lifespan.status_code}"
        )
        print(
            f"readiness before lifespan body: {ready_response_without_lifespan.json()}"
        )
    finally:
        client_without_lifespan.close()

    with TestClient(health_app) as client:
        print(f"health ready during client: {health_state['ready']}")

        live_response = client.get("/health/live")
        print(f"liveness endpoint status: {live_response.status_code}")
        print(f"liveness endpoint body: {live_response.json()}")

        ready_response = client.get("/health/ready")
        print(f"readiness endpoint status: {ready_response.status_code}")
        print(f"readiness endpoint body: {ready_response.json()}")
    print(f"health ready after client: {health_state['ready']}")

    print(f"base: {build_container_command(host='0.0.0.0', workers=1)}")
    print(f"multi: {build_container_command(host='0.0.0.0', workers=4, port=9000)}")
