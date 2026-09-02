"""Public behavior tests for P4-3 modules and imports."""

import importlib
import io
import unittest
from contextlib import redirect_stdout


class ModulesAndImportsTest(unittest.TestCase):
    def test_import_initializes_dependencies_before_attribute_access(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            note_defaults = importlib.import_module(
                "knowledge_lab.lessons.p4_3_note_defaults"
            )

        self.assertEqual(
            [
                "note defaults module started",
                "note types module started",
                "note types module finished",
                "default kind: text",
                "note defaults module finished",
            ],
            output.getvalue().splitlines(),
        )
        self.assertEqual("text", note_defaults.note_types.DEFAULT_KIND)


if __name__ == "__main__":
    unittest.main()
