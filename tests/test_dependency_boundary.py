"""Public behavior tests for P10-2 dependency boundaries."""

import unittest

from fastapi.testclient import TestClient

from knowledge_lab.lessons.p10_2_dependency_boundary import (
    app,
    build_note_label,
    execute_label_use_case,
    get_fake_label_builder,
    get_label_builder,
)


class DependencyBoundaryTest(unittest.TestCase):
    def tearDown(self) -> None:
        app.dependency_overrides.clear()

    def test_core_and_application_functions_do_not_need_fastapi_objects(self) -> None:
        self.assertEqual("Python [api]", build_note_label("Python", "api"))
        self.assertEqual(
            "TEST LABEL",
            execute_label_use_case(
                "ignored",
                "ignored",
                lambda _title, _source: "TEST LABEL",
            ),
        )

    def test_http_adapter_uses_default_provider(self) -> None:
        with TestClient(app) as client:
            response = client.get("/labels?title=Python&source=api")

        self.assertEqual(200, response.status_code)
        self.assertEqual({"label": "Python [api]"}, response.json())

    def test_dependency_override_uses_fake_and_can_be_restored(self) -> None:
        app.dependency_overrides[get_label_builder] = get_fake_label_builder
        with TestClient(app) as client:
            overridden_response = client.get("/labels?title=Python&source=api")

        self.assertEqual({"label": "FAKE LABEL"}, overridden_response.json())

        app.dependency_overrides.clear()
        with TestClient(app) as client:
            restored_response = client.get("/labels?title=Python&source=api")

        self.assertEqual({"label": "Python [api]"}, restored_response.json())


if __name__ == "__main__":
    unittest.main()
