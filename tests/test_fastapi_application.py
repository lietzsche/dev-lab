"""Public behavior tests for P9-3 FastAPI application boundaries."""

import unittest

from fastapi.testclient import TestClient

from knowledge_lab.lessons.p9_3_fastapi_application import (
    app,
    app_state,
)


class FastApiApplicationTest(unittest.TestCase):
    def test_status_endpoint_reflects_lifespan_ready_state(self) -> None:
        self.assertFalse(app_state["ready"])

        with TestClient(app) as client:
            response = client.get("/api/status")
            self.assertEqual(200, response.status_code)
            data = response.json()
            self.assertEqual("knowledge-lab", data["service"])
            self.assertEqual("running", data["status"])
            self.assertTrue(data["ready"])

        self.assertFalse(app_state["ready"])

    def test_sync_and_async_endpoints_execute_in_different_threads(self) -> None:
        with TestClient(app) as client:
            sync_res = client.get("/api/threads/sync")
            async_res = client.get("/api/threads/async")

            self.assertEqual(200, sync_res.status_code)
            self.assertEqual(200, async_res.status_code)

            sync_thread = sync_res.json()["thread"]
            async_thread = async_res.json()["thread"]

            self.assertNotEqual(sync_thread, async_thread)
            self.assertIn("worker", sync_thread.lower())

    def test_create_note_handles_validation_and_creates_note(self) -> None:
        with TestClient(app) as client:
            success_res = client.post(
                "/api/notes",
                json={
                    "title": "Public Behavior Note",
                    "content": "Testing FastAPI",
                    "tags": ["fastapi", "test"],
                },
            )
            self.assertEqual(201, success_res.status_code)
            success_data = success_res.json()
            self.assertEqual("Public Behavior Note", success_data["title"])
            self.assertEqual(["fastapi", "test"], success_data["tags"])
            self.assertTrue(success_data["created"])

            fail_res = client.post(
                "/api/notes",
                json={"title": "", "content": "Too short", "tags": []},
            )
            self.assertEqual(422, fail_res.status_code)
            fail_data = fail_res.json()
            self.assertEqual("string_too_short", fail_data["detail"][0]["type"])
            self.assertEqual(["body", "title"], fail_data["detail"][0]["loc"])

    def test_list_notes_returns_persisted_notes_via_dependency(self) -> None:
        with TestClient(app) as client:
            client.post(
                "/api/notes",
                json={
                    "title": "Listing Test Note",
                    "content": "Checked via list endpoint",
                    "tags": ["listing"],
                },
            )

            res = client.get("/api/notes")
            self.assertEqual(200, res.status_code)
            notes = res.json()
            self.assertTrue(any(n["title"] == "Listing Test Note" for n in notes))


if __name__ == "__main__":
    unittest.main()
