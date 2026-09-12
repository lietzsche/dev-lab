"""Public behavior tests for P6-2 generics and protocols."""

import unittest

from knowledge_lab.lessons.p3_3_dataclasses_and_value_objects import Note
from knowledge_lab.lessons.p6_2_generics_and_protocols import (
    BrokenRepository,
    ItemBox,
    MemoryRepository,
    Repository,
    apply_formatter,
    first,
    format_count,
    format_note,
    format_title,
    load_and_format,
)


class GenericsAndProtocolsTest(unittest.TestCase):
    def test_generic_functions_and_classes_preserve_values(self) -> None:
        self.assertEqual("Python", first(["Python", "FastAPI"]))
        self.assertEqual(10, first([10, 20]))

        text_box = ItemBox[str]("Python")
        number_box = ItemBox[int](10)

        self.assertEqual("Python", text_box.get())
        self.assertEqual(10, number_box.get())
        self.assertIs(type(text_box), type(number_box))

    def test_memory_repositories_own_independent_state(self) -> None:
        titles = MemoryRepository[str]()
        counts = MemoryRepository[int]()

        titles.save(1, "Python")
        counts.save(1, 10)

        self.assertEqual("Python", titles.get(1))
        self.assertEqual(10, counts.get(1))
        with self.assertRaises(KeyError):
            titles.get(2)

    def test_runtime_protocol_check_does_not_validate_signatures(self) -> None:
        self.assertIsInstance(MemoryRepository[str](), Repository)
        self.assertIsInstance(BrokenRepository(), Repository)

    def test_callable_contract_accepts_matching_formatters(self) -> None:
        self.assertEqual("PYTHON", apply_formatter("Python", format_title))
        self.assertEqual("10 notes", apply_formatter(10, format_count))

    def test_note_is_loaded_and_formatted_through_contracts(self) -> None:
        repository = MemoryRepository[Note]()
        note = Note(title="Python typing", content="Generic repository")
        repository.save(1, note)

        label = load_and_format(repository, 1, format_note)

        self.assertEqual("Python typing: Generic repository", label)
        self.assertIs(note, repository.get(1))
