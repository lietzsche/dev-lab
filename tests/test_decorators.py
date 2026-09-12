"""Public behavior tests for P5-4 decorators."""

import io
import unittest
from contextlib import redirect_stdout

from knowledge_lab.lessons import p5_4_decorators


class DecoratorsTest(unittest.TestCase):
    def test_log_call_forwards_arguments_and_preserves_metadata(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            result = p5_4_decorators.make_note_summary(
                "Generator",
                "Lazy execution",
                prefix="LEARN",
            )

        self.assertEqual("[LEARN] Generator: Lazy execution", result)
        self.assertEqual(
            ["before call", "after call"],
            output.getvalue().splitlines(),
        )
        self.assertEqual(
            "make_note_summary",
            p5_4_decorators.make_note_summary.__name__,
        )

    def test_measure_time_preserves_the_original_result(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            result = p5_4_decorators.count_characters("Python")

        self.assertEqual(6, result)
        self.assertRegex(
            output.getvalue().strip(),
            r"^elapsed seconds: \d+\.\d{6}$",
        )

    def test_decorator_factory_preserves_category_and_metadata(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            result = p5_4_decorators.format_title("Python")

        self.assertEqual("PYTHON", result)
        self.assertEqual("wrapper called: learning", output.getvalue().strip())
        self.assertEqual("format_title", p5_4_decorators.format_title.__name__)

    def test_route_registers_and_returns_the_original_function(self) -> None:
        registered = p5_4_decorators.routes["/notes"]

        self.assertIs(p5_4_decorators.list_notes, registered)
        self.assertEqual(["Python", "Generator"], registered())
