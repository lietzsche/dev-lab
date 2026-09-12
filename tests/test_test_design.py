"""Exercises for P6-3 test design."""

import unittest
from unittest.mock import Mock

import pytest

from knowledge_lab.lessons.p3_3_dataclasses_and_value_objects import Note
from knowledge_lab.lessons.p3_4_protocols_and_composition import (
    InMemoryNoteRepository,
    NoteRepository,
    NoteService,
)
from knowledge_lab.lessons.p6_3_test_design import normalize_title


class FakeNoteRepository:
    def __init__(self) -> None:
        self.notes: list[Note] = []

    def add(self, note: Note) -> None:
        self.notes.append(note)

    def all(self) -> list[Note]:
        return self.notes.copy()


@pytest.fixture
def service_with_fake() -> tuple[NoteService, FakeNoteRepository]:
    fake = FakeNoteRepository()
    return NoteService(fake), fake


class StubNoteRepository:
    def __init__(self, notes: list[Note]) -> None:
        self.notes: list[Note] = notes

    def add(self, note: Note) -> None:
        return None

    def all(self) -> list[Note]:
        return self.notes


class NoteServiceIntegrationTest(unittest.TestCase):
    def test_created_note_is_available_through_service(self) -> None:
        # given
        service = NoteService(InMemoryNoteRepository())

        # when
        note = service.create_note(title="Python testing", content="Test boundary")
        notes = service.list_notes()

        # then
        self.assertEqual([note], notes)


class NoteServiceUnitTest(unittest.TestCase):
    def test_list_notes_returns_stubbed_notes(self) -> None:
        # given
        ready_notes = [Note("Stub title", "Stub content")]
        stub = StubNoteRepository(ready_notes)
        service = NoteService(stub)

        # when
        result_notes = service.list_notes()

        # then
        self.assertEqual(ready_notes, result_notes)

    def test_create_note_calls_repository_add_once(self) -> None:
        # given
        repository = Mock(spec=NoteRepository)
        service = NoteService(repository)

        # when
        note = service.create_note("Python mock", "Interaction")

        # then
        repository.add.assert_called_once_with(note)


@pytest.mark.parametrize(
    ("title", "expected"),
    [
        (" Python testing ", "Python testing"),
        ("Python", "Python"),
        (" ", ""),
    ],
)
def test_normalize_title_removes_outer_whitespace(title: str, expected: str) -> None:
    # when
    result = normalize_title(title)

    # then
    assert result == expected


def test_create_note_stores_note_in_fake_repository(
    service_with_fake: tuple[NoteService, FakeNoteRepository],
) -> None:
    # given
    service, fake = service_with_fake

    # when
    note = service.create_note("new title", "new content")

    # then
    assert fake.all() == [note]


def test_fake_service_starts_with_no_notes(
    service_with_fake: tuple[NoteService, FakeNoteRepository],
) -> None:
    # given
    service, _ = service_with_fake

    # then
    assert service.list_notes() == []
