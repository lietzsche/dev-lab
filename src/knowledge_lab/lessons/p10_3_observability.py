"""P10-3: observability 경계를 관찰한다."""

from contextlib import contextmanager
from contextvars import ContextVar
import io
import json
import logging
import time
from typing import Iterator


current_request_id: ContextVar[str | None] = ContextVar("request_id", default=None)


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "level": record.levelname,
            "message": record.getMessage(),
            "name": record.name,
        }
        if getattr(record, "event", None):
            payload["event"] = getattr(record, "event")
        if getattr(record, "note_id", None):
            payload["note_id"] = getattr(record, "note_id")
        req_id = current_request_id.get()
        if req_id is not None:
            payload["request_id"] = req_id
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False)


class MetricsCollector:
    def __init__(self) -> None:
        self.request_count: int = 0
        self.error_count: int = 0
        self.total_duration_ms: float = 0
        self.last_duration_ms: float = 0

    @contextmanager
    def track(self) -> Iterator[None]:
        self.request_count += 1
        start = time.perf_counter()
        try:
            yield
        except Exception:
            self.error_count += 1
            raise
        finally:
            duration = (time.perf_counter() - start) * 1000
            self.last_duration_ms = duration
            self.total_duration_ms += duration


@contextmanager
def bind_request_id(request_id: str) -> Iterator[None]:
    token = current_request_id.set(request_id)
    try:
        yield
    finally:
        current_request_id.reset(token)


def setup_memory_logger(
    name: str = "knowledge_lab.observability",
) -> tuple[logging.Logger, io.StringIO]:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    buffer = io.StringIO()
    handler = logging.StreamHandler(buffer)
    handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s:%(message)s"))
    logger.addHandler(handler)
    return logger, buffer


def setup_json_logger(
    name: str = "knowledge_lab.structured",
) -> tuple[logging.Logger, io.StringIO]:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    buffer = io.StringIO()
    handler = logging.StreamHandler(buffer)
    handler.setFormatter(JsonFormatter())
    logger.addHandler(handler)
    return logger, buffer


def handle_note_request(note_id: int, logger: logging.Logger) -> dict[str, str]:
    try:
        if note_id <= 0:
            raise ValueError(f"유효하지 않은 노트 ID: {note_id}")
        return {"status": "ok", "note_id": str(note_id)}
    except Exception:
        logger.error(
            "노트 처리 실패",
            exc_info=True,
            extra={"note_id": note_id, "event": "note_error"},
        )
        return {"error": "요청을 처리할 수 없습니다", "code": "INVALID_NOTE"}


def run() -> None:
    """Run the current observability exercise."""
    print()
    print("P10-3 observability 시작")

    json_logger, buffer = setup_json_logger()
    collector = MetricsCollector()
    with collector.track():
        response = handle_note_request(-1, json_logger)
        print(f"response: {response}")
        print(f"internal: {buffer.getvalue().strip()}")
    try:
        with collector.track():
            raise ValueError("유효하지 않은 노트 ID")
    except ValueError as error:
        print(f"error: {error}")
    print(f"collector request count: {collector.request_count}")
    print(f"collector error count: {collector.error_count}")
    print(f"collector total duration ms > 0: {collector.total_duration_ms > 0}")
