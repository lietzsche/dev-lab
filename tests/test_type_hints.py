"""Public behavior tests for P6-1 type hints."""

import unittest
from typing import Any

from knowledge_lab.lessons.p3_3_dataclasses_and_value_objects import Note, Tag
from knowledge_lab.lessons.p6_1_type_hints import (
    create_note,
    format_note_id,
    normalize_source,
    normalize_tags,
    read_title,
    repeat_title,
)


class TypeHintsTest(unittest.TestCase):
    def test_annotations_do_not_enforce_runtime_types(self) -> None:
        unchecked_repeat: Any = repeat_title

        self.assertEqual(6, unchecked_repeat(3, 2))
        self.assertIs(Any, read_title.__annotations__["payload"])

        with self.assertRaises(TypeError):
            read_title(42)

    def test_union_and_optional_inputs_are_normalized(self) -> None:
        self.assertEqual("note-42", format_note_id(42))
        self.assertEqual("custom", format_note_id(" custom "))
        self.assertEqual("unknown", normalize_source())
        self.assertEqual("API", normalize_source(" API "))

    def test_normalize_tags_returns_a_new_list(self) -> None:
        tags = [" Python ", "TYPING"]

        normalized = normalize_tags(tags)

        self.assertEqual(["python", "typing"], normalized)
        self.assertEqual([" Python ", "TYPING"], tags)
        self.assertIsNot(tags, normalized)

    def test_create_note_builds_domain_objects_without_mutating_input(self) -> None:
        tags = [" Python ", "TYPING"]

        note = create_note(" Type hints ", tags)

        self.assertEqual(
            Note(
                title="Type hints",
                content="",
                tags=[Tag(name="python"), Tag(name="typing")],
            ),
            note,
        )
        self.assertEqual([" Python ", "TYPING"], tags)
