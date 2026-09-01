"""Public behavior tests for P4-2 context managers."""

import io
import unittest
from contextlib import redirect_stdout

from knowledge_lab.lessons.p4_2_context_managers import (
    ManagedStream,
    managed_text_stream,
)


class ContextManagersTest(unittest.TestCase):
    def test_class_context_manager_closes_owned_stream(self) -> None:
        manager = ManagedStream("class resource")

        with redirect_stdout(io.StringIO()):
            with manager as stream:
                self.assertIs(stream, manager.stream)
                self.assertFalse(stream.closed)

        self.assertTrue(manager.stream.closed)

    def test_class_context_manager_propagates_exception_by_default(self) -> None:
        manager = ManagedStream("failed class resource")

        with redirect_stdout(io.StringIO()):
            with self.assertRaisesRegex(RuntimeError, "class failure"):
                with manager:
                    raise RuntimeError("class failure")

        self.assertTrue(manager.stream.closed)

    def test_generator_context_manager_closes_stream_after_exception(self) -> None:
        stream = None

        with self.assertRaisesRegex(RuntimeError, "generator failure"):
            with managed_text_stream("generator resource") as stream:
                self.assertFalse(stream.closed)
                raise RuntimeError("generator failure")

        self.assertIsNotNone(stream)
        self.assertTrue(stream.closed)


if __name__ == "__main__":
    unittest.main()
