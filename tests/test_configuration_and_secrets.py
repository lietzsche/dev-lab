"""Public behavior tests for P10-1 configuration boundaries."""

import io
import os
import unittest
from contextlib import redirect_stdout
from dataclasses import FrozenInstanceError
from unittest.mock import patch

from knowledge_lab.lessons.p10_1_configuration_and_secrets import load_settings, run


class ConfigurationAndSecretsTest(unittest.TestCase):
    def test_defaults_create_immutable_settings(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            settings = load_settings()

        self.assertEqual(8000, settings.http_port)
        self.assertEqual("development", settings.mode)
        self.assertIsNone(settings.api_token)
        with self.assertRaises(FrozenInstanceError):
            settings.http_port = 9000

    def test_environment_overrides_are_loaded_without_exposing_token_in_repr(
        self,
    ) -> None:
        with patch.dict(
            os.environ,
            {
                "KNOWLEDGE_LAB_PORT": "9000",
                "KNOWLEDGE_LAB_MODE": "production",
                "KNOWLEDGE_LAB_API_TOKEN": "demo-token",
            },
            clear=True,
        ):
            settings = load_settings()

        self.assertEqual(9000, settings.http_port)
        self.assertEqual("production", settings.mode)
        self.assertEqual("demo-token", settings.api_token)
        self.assertNotIn("demo-token", repr(settings))

    def test_production_requires_nonempty_token(self) -> None:
        for token in (None, ""):
            with self.subTest(token=token):
                environment = {"KNOWLEDGE_LAB_MODE": "production"}
                if token is not None:
                    environment["KNOWLEDGE_LAB_API_TOKEN"] = token
                with patch.dict(os.environ, environment, clear=True):
                    with self.assertRaises(ValueError):
                        load_settings()

    def test_test_mode_does_not_require_token(self) -> None:
        with patch.dict(os.environ, {"KNOWLEDGE_LAB_MODE": "test"}, clear=True):
            settings = load_settings()

        self.assertEqual("test", settings.mode)
        self.assertIsNone(settings.api_token)

    def test_invalid_port_and_mode_are_rejected(self) -> None:
        for port in ("0", "65536", "not-a-number"):
            with self.subTest(port=port):
                with patch.dict(os.environ, {"KNOWLEDGE_LAB_PORT": port}, clear=True):
                    with self.assertRaises(ValueError):
                        load_settings()

        with patch.dict(os.environ, {"KNOWLEDGE_LAB_MODE": "unknown"}, clear=True):
            with self.assertRaises(ValueError):
                load_settings()

    def test_run_does_not_print_token(self) -> None:
        output = io.StringIO()
        with patch.dict(
            os.environ, {"KNOWLEDGE_LAB_API_TOKEN": "demo-token"}, clear=True
        ):
            with redirect_stdout(output):
                run()

        self.assertIn("api_token is not None: True", output.getvalue())
        self.assertNotIn("demo-token", output.getvalue())


if __name__ == "__main__":
    unittest.main()
