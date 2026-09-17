"""P9-1: HTTP request와 response의 transport 경계를 관찰한다."""

import json
from collections.abc import Iterator
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


class _NoteRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        content_length = int(self.headers.get("Content-Length", "0"))
        self.rfile.read(content_length)

        if urlsplit(self.path).path == "/notes":
            status = 201
            response_body = b'{"id": 1, "title": "Python"}'
        else:
            status = 404
            response_body = b'{"error": "note not found"}'

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response_body)))
        self.end_headers()
        self.wfile.write(response_body)

    def log_message(self, format: str, *args: object) -> None:
        pass


@contextmanager
def local_note_server() -> Iterator[str]:
    server = HTTPServer(("127.0.0.1", 0), _NoteRequestHandler)
    server_thread = Thread(
        target=server.serve_forever,
        name="note-http-server",
    )
    server_thread.start()

    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        server_thread.join()


def build_note_request(
    url: str,
    body: bytes,
    request_id: str,
) -> Request:
    return Request(
        url=url,
        data=body,
        method="POST",
        headers={"Content-Type": "application/json", "X-Request-ID": request_id},
    )


def serialize_json(data: dict[str, object]) -> str:
    return json.dumps(data, ensure_ascii=False)


def encode_http_body(json_text: str) -> bytes:
    return json_text.encode(encoding="utf-8")


def send_note_request(
    request: Request,
    timeout_seconds: float,
) -> tuple[int, str | None, bytes]:
    with urlopen(request, timeout=timeout_seconds) as response:
        status = response.status
        content_type = response.headers.get("Content-Type")
        body = response.read()
        print(f"second read: {response.read()!r}")
        print(f"in block response.closed: {response.closed}")
    print(f"after block response.closed: {response.closed}")
    return (status, content_type, body)


def decode_http_body(body: bytes) -> str:
    return body.decode(encoding="utf-8")


def deserialize_json(json_text: str) -> object:
    return json.loads(json_text)


def observe_http_error(
    request: Request,
    timeout_seconds: float,
) -> None:
    try:
        send_note_request(request, timeout_seconds)
    except HTTPError as error:
        with error:
            print(f"error type: {type(error)}")
            error_code = error.code
            error_read = error.read()
            print(f"error code: {error_code}, type: {type(error_code)}")
            print(f"error reason: {error.reason}")
            print(f"error content type: {error.headers.get('Content-Type')}")
            print(f"error read: {error_read!r}, type: {type(error_read)}")
            print(f"in block error.closed: {error.closed}")
        print(f"after block error.closed: {error.closed}")


def observe_network_error(
    request: Request,
    timeout_seconds: float,
) -> None:
    try:
        send_note_request(request, timeout_seconds)
    except HTTPError:
        raise
    except URLError as error:
        print(f"error type: {type(error)}")
        print(f"error reason repr: {error.reason!r}")
        print(f"error reason type: {type(error.reason)}")
        print(f"error is HTTPError instance: {isinstance(error, HTTPError)}")
        print(f"error has attr code: {hasattr(error, 'code')}")


def run() -> None:
    """Run the current HTTP boundary exercise."""
    print()
    print("P9-1 HTTP boundary 시작")

    note_data: dict[str, object] = {
        "title": "파이썬 HTTP",
        "tags": ["python", "http"],
        "published": False,
    }
    json_text = serialize_json(note_data)
    body = encode_http_body(json_text)
    with local_note_server() as base_url:
        closed_server_url = f"{base_url}/notes"
    request = build_note_request(closed_server_url, body, "req-1")
    observe_network_error(request, 0.5)
