"""Public behavior tests for P9-4 API and operations boundaries."""

import json
import os
import unittest
from unittest.mock import patch
from urllib.request import urlopen

from fastapi.testclient import TestClient

from knowledge_lab.lessons.p9_4_api_testing_and_operations import (
    get_runtime_mode,
    job_results,
    job_state,
    live_server,
    slow_completed,
    test_app as api_app,
)


class ApiTestingAndOperationsTest(unittest.TestCase):
    def setUp(self) -> None:
        job_state["count"] = 0
        job_results.clear()
        slow_completed.clear()

    def test_probe_works_in_process_and_over_loopback_http(self) -> None:
        with TestClient(api_app) as client:
            response = client.get("/probe")
            self.assertEqual(200, response.status_code)
            self.assertEqual({"pid": os.getpid()}, response.json())

        with live_server(api_app) as base_url:
            with urlopen(f"{base_url}/probe", timeout=2.0) as response:
                self.assertEqual(200, response.status)
                self.assertEqual({"pid": os.getpid()}, json.load(response))

    def test_missing_note_is_mapped_to_http_error(self) -> None:
        with TestClient(api_app) as client:
            response = client.get("/notes/42")

        self.assertEqual(404, response.status_code)
        self.assertEqual(
            {
                "error": "note_not_found",
                "message": "note not found: 42",
                "path": "/notes/42",
            },
            response.json(),
        )

    def test_runtime_mode_reads_environment_at_call_time(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual("development", get_runtime_mode())
            os.environ["KNOWLEDGE_LAB_MODE"] = "production"
            self.assertEqual("production", get_runtime_mode())

    def test_client_timeout_does_not_cancel_server_work(self) -> None:
        with live_server(api_app) as base_url:
            with self.assertRaises(TimeoutError):
                urlopen(f"{base_url}/slow", timeout=0.2)
            self.assertTrue(slow_completed.wait(timeout=2.0))

    def test_idempotency_key_reuses_original_result(self) -> None:
        with TestClient(api_app) as client:
            first = client.post("/jobs", headers={"Idempotency-Key": "job-a"})
            retry = client.post("/jobs", headers={"Idempotency-Key": "job-a"})
            second = client.post("/jobs", headers={"Idempotency-Key": "job-b"})
            late_retry = client.post("/jobs", headers={"Idempotency-Key": "job-a"})
            missing_key = client.post("/jobs")

        self.assertEqual(
            [200] * 4, [r.status_code for r in (first, retry, second, late_retry)]
        )
        self.assertEqual(422, missing_key.status_code)
        self.assertEqual(
            [{"count": 1}, {"count": 1}, {"count": 2}, {"count": 1}],
            [r.json() for r in (first, retry, second, late_retry)],
        )
        self.assertEqual(2, job_state["count"])

    def test_pagination_keeps_total_and_validates_limits(self) -> None:
        with TestClient(api_app) as client:
            for key in ("job-c", "job-a", "job-b"):
                response = client.post("/jobs", headers={"Idempotency-Key": key})
                self.assertEqual(200, response.status_code)

            first_page = client.get("/jobs?offset=0&limit=2")
            second_page = client.get("/jobs?offset=2&limit=2")
            invalid_limit = client.get("/jobs?limit=0")
            invalid_offset = client.get("/jobs?offset=-1")

        self.assertEqual(200, first_page.status_code)
        self.assertEqual(200, second_page.status_code)
        self.assertEqual(
            {
                "items": [{"key": "job-a", "count": 2}, {"key": "job-b", "count": 3}],
                "total": 3,
            },
            first_page.json(),
        )
        self.assertEqual(
            {"items": [{"key": "job-c", "count": 1}], "total": 3},
            second_page.json(),
        )
        self.assertEqual(422, invalid_limit.status_code)
        self.assertEqual(422, invalid_offset.status_code)
        self.assertEqual(3, job_state["count"])


if __name__ == "__main__":
    unittest.main()
