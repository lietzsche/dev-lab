"""Public behavior tests for P9-2 Pydantic validation boundaries."""

import unittest

from pydantic import ValidationError

from knowledge_lab.lessons.p3_3_dataclasses_and_value_objects import Note, Tag
from knowledge_lab.lessons.p9_2_pydantic_validation import (
    NoteCreatePayload,
    to_domain_note,
)


class PydanticValidationTest(unittest.TestCase):
    def test_constraints_produce_structured_validation_errors(self) -> None:
        with self.assertRaises(ValidationError) as raised:
            NoteCreatePayload.model_validate(
                {"title": "", "content": "Validation", "tags": []}
            )

        details = raised.exception.errors()

        self.assertEqual(1, raised.exception.error_count())
        self.assertEqual(("title",), details[0]["loc"])
        self.assertEqual("string_too_short", details[0]["type"])
        self.assertEqual("", details[0]["input"])

    def test_default_parsing_accepts_tuple_but_strict_validation_rejects_it(
        self,
    ) -> None:
        raw_payload: dict[str, object] = {
            "title": "Parsing",
            "content": "Tuple to list",
            "tags": ("python", "pydantic"),
        }

        payload = NoteCreatePayload.model_validate(raw_payload)

        self.assertEqual(["python", "pydantic"], payload.tags)
        self.assertIsInstance(payload.tags, list)
        self.assertIsInstance(raw_payload["tags"], tuple)
        with self.assertRaises(ValidationError) as raised:
            NoteCreatePayload.model_validate(raw_payload, strict=True)
        self.assertEqual("list_type", raised.exception.errors()[0]["type"])

    def test_json_serialization_round_trip_creates_an_equal_model(self) -> None:
        payload = NoteCreatePayload(
            title="Serialization",
            content="JSON round trip",
            tags=["python"],
        )

        json_text = payload.model_dump_json()
        restored = NoteCreatePayload.model_validate_json(json_text)

        self.assertIsInstance(payload.model_dump(), dict)
        self.assertIsInstance(json_text, str)
        self.assertEqual(payload, restored)
        self.assertIsNot(payload, restored)

    def test_transport_payload_maps_to_separate_domain_objects(self) -> None:
        payload = NoteCreatePayload(
            title="Boundary",
            content="Transport to domain",
            tags=["python", "pydantic"],
        )

        note = to_domain_note(payload)

        self.assertIsInstance(note, Note)
        self.assertEqual(payload.title, note.title)
        self.assertEqual(payload.content, note.content)
        self.assertEqual([Tag("python"), Tag("pydantic")], note.tags)
        self.assertIsNot(payload.tags, note.tags)
        self.assertIsInstance(payload.tags[0], str)
        self.assertIsInstance(note.tags[0], Tag)


if __name__ == "__main__":
    unittest.main()
