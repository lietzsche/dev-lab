"""Public behavior tests for P9-1 HTTP boundaries."""

import io
import unittest
from contextlib import redirect_stdout
from urllib.error import URLError
from urllib.parse import urlsplit
from unittest.mock import patch

from knowledge_lab.lessons.p9_1_http_boundary import (
    build_note_request,
    decode_http_body,
    deserialize_json,
    encode_http_body,
    local_note_server,
    observe_http_error,
    observe_network_error,
    send_note_request,
    serialize_json,
)


class HttpBoundaryTest(unittest.TestCase):
    def test_request_keeps_transport_components_separate(self) -> None:
        body = b'{"title": "Python"}'
        request = build_note_request(
            "http://localhost:8000/notes?source=lab",
            body,
            "req-1",
        )
        url_parts = urlsplit(request.full_url)

        self.assertEqual("POST", request.get_method())
        self.assertEqual("/notes", url_parts.path)
        self.assertEqual("source=lab", url_parts.query)
        self.assertEqual("application/json", request.get_header("Content-type"))
        self.assertEqual("req-1", request.get_header("X-request-id"))
        self.assertIs(body, request.data)

    def test_json_round_trip_crosses_text_and_bytes_boundaries(self) -> None:
        data: dict[str, object] = {
            "title": "파이썬 HTTP",
            "published": False,
        }

        json_text = serialize_json(data)
        body = encode_http_body(json_text)
        restored = deserialize_json(decode_http_body(body))

        self.assertIsInstance(json_text, str)
        self.assertIsInstance(body, bytes)
        self.assertGreater(len(body), len(json_text))
        self.assertEqual(data, restored)

    def test_success_response_exposes_status_headers_and_body(self) -> None:
        with local_note_server() as base_url:
            request = build_note_request(
                f"{base_url}/notes",
                b'{"title": "Python"}',
                "req-1",
            )
            with redirect_stdout(io.StringIO()):
                status, content_type, body = send_note_request(request, 1.0)

        self.assertEqual(201, status)
        self.assertEqual("application/json", content_type)
        self.assertEqual({"id": 1, "title": "Python"}, deserialize_json(body.decode()))

    def test_http_error_retains_response_details(self) -> None:
        output = io.StringIO()

        with local_note_server() as base_url:
            request = build_note_request(
                f"{base_url}/missing",
                b"{}",
                "req-2",
            )
            with redirect_stdout(output):
                observe_http_error(request, 1.0)

        self.assertIn("error code: 404", output.getvalue())
        self.assertIn("error reason: Not Found", output.getvalue())
        self.assertIn("after block error.closed: True", output.getvalue())

    def test_network_error_retains_lower_level_reason(self) -> None:
        request = build_note_request("http://127.0.0.1/notes", b"{}", "req-3")
        reason = ConnectionRefusedError(111, "Connection refused")
        output = io.StringIO()

        with (
            patch(
                "knowledge_lab.lessons.p9_1_http_boundary.send_note_request",
                side_effect=URLError(reason),
            ),
            redirect_stdout(output),
        ):
            observe_network_error(request, 0.5)

        self.assertIn(
            "error reason type: <class 'ConnectionRefusedError'>", output.getvalue()
        )
        self.assertIn("error is HTTPError instance: False", output.getvalue())
        self.assertIn("error has attr code: False", output.getvalue())


if __name__ == "__main__":
    unittest.main()
