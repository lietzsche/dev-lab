"""P9-3: FastAPI application과 route, dependency, endpoint 실행 모델을 관찰한다."""

from contextlib import asynccontextmanager
from typing import AsyncIterator
import threading
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from knowledge_lab.lessons.p3_4_protocols_and_composition import (
    InMemoryNoteRepository,
    NoteService,
)
from knowledge_lab.lessons.p9_2_pydantic_validation import (
    NoteCreatePayload,
    to_domain_note,
)


_repo = InMemoryNoteRepository()
_service = NoteService(_repo)


def get_note_service() -> NoteService:
    return _service


app_state: dict[str, bool] = {"ready": False}


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    app_state["ready"] = True
    try:
        yield
    finally:
        app_state["ready"] = False


app = FastAPI(lifespan=lifespan)


@app.get("/api/status")
def get_status() -> dict[str, str | bool]:
    return {
        "service": "knowledge-lab",
        "status": "running",
        "ready": app_state["ready"],
    }


@app.get("/api/threads/sync")
def inspect_sync_thread() -> dict[str, str]:
    return {"thread": threading.current_thread().name}


@app.get("/api/threads/async")
async def inspect_async_thread() -> dict[str, str]:
    return {"thread": threading.current_thread().name}


@app.post("/api/notes", status_code=201)
def create_note_endpoint(
    payload: NoteCreatePayload, service: NoteService = Depends(get_note_service)
) -> dict[str, object]:
    domain_note = to_domain_note(payload)
    service.repository.add(domain_note)
    return {
        "title": domain_note.title,
        "tags": [t.name for t in domain_note.tags],
        "created": True,
    }


@app.get("/api/notes")
def list_notes_endpoint(
    service: NoteService = Depends(get_note_service),
) -> list[dict[str, object]]:
    return [
        {
            "title": note.title,
            "content": note.content,
            "tags": [t.name for t in note.tags],
        }
        for note in service.list_notes()
    ]


def run() -> None:
    """Run the current FastAPI application exercise."""
    print()
    print("P9-3 FastAPI application 시작")

    client = TestClient(app)
    response = client.get("/api/status")
    print(f"status code: {response.status_code}")
    print(f"content type: {response.headers.get('content-type')}")
    print(f"json body: {response.json()}")

    print(f"async thread name: {client.get('/api/threads/async').json()['thread']}")
    print(f"sync thread name: {client.get('/api/threads/sync').json()['thread']}")

    success_response = client.post(
        "/api/notes",
        json={
            "title": "FastAPI Note",
            "content": "Automatic validation",
            "tags": ["fastapi", "web"],
        },
    )
    failure_response = client.post(
        "/api/notes", json={"title": "", "content": "Invalid", "tags": []}
    )
    print(f"success response status code: {success_response.status_code}")
    print(f"success response json: {success_response.json()}")
    print(f"failure response status code: {failure_response.status_code}")
    print(f"failure response json: {failure_response.json()['detail'][0]['type']}")

    list_notes_response = client.get("/api/notes").json()
    print(f"notes all list: {list_notes_response}")

    with TestClient(app) as context_client:
        print(f"in block status_response: {context_client.get('/api/status').json()}")
    print(f"after block status_response: {context_client.get('/api/status').json()}")
