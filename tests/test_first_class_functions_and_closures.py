"""Public behavior tests for P5-1 functions and closures."""

import unittest

from knowledge_lab.lessons.p5_1_first_class_functions_and_closures import (
    apply_title_formatter,
    format_note_title,
    make_note_counter,
    make_note_formatter,
    make_prefix_readers,
)


class FirstClassFunctionsAndClosuresTest(unittest.TestCase):
    def test_function_object_can_be_passed_as_an_argument(self) -> None:
        self.assertEqual(
            "[NOTE] First-class function",
            apply_title_formatter(format_note_title, "First-class function"),
        )

    def test_formatter_factories_own_independent_closure_cells(self) -> None:
        note_formatter = make_note_formatter("[NOTE]")
        todo_formatter = make_note_formatter("[TODO]")

        self.assertEqual("[NOTE] Closure", note_formatter("Closure"))
        self.assertEqual("[TODO] Closure", todo_formatter("Closure"))
        self.assertIsNot(
            note_formatter.__closure__[0],
            todo_formatter.__closure__[0],
        )

    def test_prefix_readers_avoid_loop_late_binding(self) -> None:
        readers = make_prefix_readers(["[NOTE]", "[TODO]", "[DONE]"])

        self.assertEqual(
            ["[NOTE]", "[TODO]", "[DONE]"],
            [reader() for reader in readers],
        )
        self.assertIsNot(readers[0].__closure__[0], readers[-1].__closure__[0])

    def test_counter_preserves_state_between_calls(self) -> None:
        counter = make_note_counter()

        self.assertEqual(1, counter())
        self.assertEqual(2, counter())


if __name__ == "__main__":
    unittest.main()
