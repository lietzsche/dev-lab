"""P9-4: API test와 운영 경계를 관찰한다."""

import asyncio
import logging
import os
import socket
import sys
import threading
import time
from collections.abc import Iterator
from contextlib import contextmanager

import uvicorn
from fastapi import FastAPI, Header, Request, Query
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient

from knowledge_lab.lessons.p4_1_exceptions import NoteNotFoundError


slow_completed = threading.Event()


job_state = {"count": 0}


job_results: dict[str, int] = {}


logger = logging.getLogger(__name__)
test_app = FastAPI()


@test_app.get("/probe")
def probe_process() -> dict[str, int]:
    return {"pid": os.getpid()}


@contextmanager
def live_server(app: FastAPI) -> Iterator[str]:
    """Run an ASGI app on a temporary loopback TCP port."""
    server_socket = socket.socket()
    server_socket.bind(("127.0.0.1", 0))
    server_socket.listen()
    host, port = server_socket.getsockname()

    server = uvicorn.Server(uvicorn.Config(app, log_level="critical"))
    server_thread = threading.Thread(
        target=server.run,
        kwargs={"sockets": [server_socket]},
        daemon=True,
        name="uvicorn-test-server",
    )
    server_thread.start()

    try:
        while not server.started:
            if not server_thread.is_alive():
                raise RuntimeError("test server stopped before startup")
            time.sleep(0.01)
        yield f"http://{host}:{port}"
    finally:
        server.should_exit = True
        server_thread.join(timeout=2.0)
        server_socket.close()
        if server_thread.is_alive():
            raise RuntimeError("test server did not stop")


@contextmanager
def show_lesson_logs() -> Iterator[None]:
    """Show this lesson's logs without changing global logging state."""
    log_handler = logging.StreamHandler(sys.stdout)
    log_handler.setFormatter(logging.Formatter("%(levelname)s %(name)s %(message)s"))
    previous_level = logger.level
    previous_propagate = logger.propagate
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    try:
        yield
    finally:
        logger.removeHandler(log_handler)
        logger.setLevel(previous_level)
        logger.propagate = previous_propagate


@test_app.get("/notes/{note_id}")
def get_missing_note(note_id: int) -> dict[str, object]:
    raise NoteNotFoundError(f"note not found: {note_id}")


@test_app.exception_handler(NoteNotFoundError)
async def handle_note_not_found(
    request: Request,
    error: NoteNotFoundError,
) -> JSONResponse:
    logger.info(
        "event=note_not_found, path=%s, error_type=%s",
        request.url.path,
        type(error).__name__,
    )
    return JSONResponse(
        status_code=404,
        content={
            "error": "note_not_found",
            "message": str(error),
            "path": request.url.path,
        },
    )


@test_app.get("/slow")
async def slow_probe() -> dict[str, bool]:
    await asyncio.sleep(1.0)
    slow_completed.set()
    return {"completed": True}


def get_runtime_mode() -> str:
    return os.getenv("KNOWLEDGE_LAB_MODE", "development")


@test_app.post("/jobs")
def create_job(
    idempotency_key: str = Header(alias="Idempotency-Key"),
) -> dict[str, int]:
    count = job_state.get("count", 0)
    if idempotency_key in job_results:
        return {"count": job_results[idempotency_key]}
    count += 1
    job_state["count"] = count
    job_results[idempotency_key] = job_state["count"]
    return {"count": count}


@test_app.get("/jobs")
def list_jobs(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=2, ge=1, le=50),
) -> dict[str, object]:
    sorted_job_results = sorted(job_results)
    items = sorted_job_results[offset : offset + limit]
    return {
        "items": [{"key": key, "count": job_results[key]} for key in items],
        "total": len(sorted_job_results),
    }


def run() -> None:
    """Run the current API testing and operations exercise."""
    print()
    print("P9-4 API test와 운영 경계 시작")

    job_state["count"] = 0
    job_results.clear()
    with TestClient(test_app) as client:
        for name in ["a", "b", "c"]:
            client.post("/jobs", headers={"Idempotency-Key": f"job-{name}"}).json()
        print(f"page 1: {client.get('/jobs?offset=0&limit=2').json()}")
        print(f"page 2: {client.get('/jobs?offset=2&limit=2').json()}")
        print(f"invalid limit status: {client.get('/jobs?limit=0').status_code}")
        print(f"job_state: {job_state}")
