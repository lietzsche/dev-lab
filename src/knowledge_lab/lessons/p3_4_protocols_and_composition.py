"""P3-4: protocols and composition."""

from typing import Protocol, runtime_checkable

from knowledge_lab.lessons.p3_3_dataclasses_and_value_objects import Note


@runtime_checkable
class Formatter(Protocol):
    def format(self, value: str) -> str:
        ...


class NoteFormatter:
    def format(self, title: str) -> str:
        return f"Note: {title}"


class UppercaseFormatter:
    def format(self, title: str) -> str:
        return f"NOTE: {title.upper()}"


class BrokenFormatter:
    def format(self) -> str:
        return "I don't have title"


class NotePresenter:
    def __init__(self, formatter: Formatter) -> None:
        self.formatter = formatter

    def present(self, title: str) -> str:
        return self.formatter.format(title)


@runtime_checkable
class NoteRepository(Protocol):
    def add(self, note: Note) -> None:
        ...

    def all(self) -> list[Note]:
        ...


class InMemoryNoteRepository:
    def __init__(self) -> None:
        self._notes = []

    def add(self, note: Note) -> None:
        self._notes.append(note)

    def all(self) -> list[Note]:
        return self._notes.copy()


class NoteService:
    def __init__(self, repository: NoteRepository) -> None:
        self.repository = repository

    def create_note(self, title: str, content: str) -> Note:
        note = Note(title, content)
        self.repository.add(note)
        return note

    def list_notes(self) -> list[Note]:
        return self.repository.all()


def run() -> None:
    """Run protocol and composition experiments added during P3-4."""
    print()
    print("Run protocol and composition experiments added during P3-4.")

    note_formatter = NoteFormatter()
    note_presenter = NotePresenter(note_formatter)
    print(
        "note_presenter.formatter is note_formatter: "
        f"{note_presenter.formatter is note_formatter}"
    )
    print(f"presenter.present: {note_presenter.present('this is good title')}")

    uppercase_formatter = UppercaseFormatter()
    print(
        "isinstance(uppercase_formatter, NoteFormatter): "
        f"{isinstance(uppercase_formatter, NoteFormatter)}"
    )
    note_presenter = NotePresenter(uppercase_formatter)
    print(f"note_presenter.present: {note_presenter.present('this it new title')}")

    print(
        "isinstance(note_formatter, Formatter): "
        f"{isinstance(note_formatter, Formatter)}"
    )
    print(
        "isinstance(uppercase_formatter, Formatter): "
        f"{isinstance(uppercase_formatter, Formatter)}"
    )
    print(
        "Formatter in NoteFormatter.__mro__: "
        f"{Formatter in NoteFormatter.__mro__}"
    )
    print(
        "Formatter in UppercaseFormatter.__mro__: "
        f"{Formatter in UppercaseFormatter.__mro__}"
    )

    broken_formatter = BrokenFormatter()
    print(
        "isinstance(broken_formatter, Formatter): "
        f"{isinstance(broken_formatter, Formatter)}"
    )
    note_presenter = NotePresenter(broken_formatter)
    # note_presenter.present("this is nice title")  # TypeError 관찰 완료

    in_memory_repository = InMemoryNoteRepository()
    print(
        "isinstance(in_memory_repository, NoteRepository): "
        f"{isinstance(in_memory_repository, NoteRepository)}"
    )
    in_memory_repository.add(Note("good note", "good content"))
    all_note_list = in_memory_repository.all()
    print(f"in memory note all: {all_note_list}")
    print(
        "in memory note all is in_memory_repository._notes: "
        f"{in_memory_repository.all() is in_memory_repository._notes}"
    )

    new_repository = InMemoryNoteRepository()
    note_service = NoteService(new_repository)
    print(f"id(note_service.repository): {id(note_service.repository)}")
    print(f"id(new_repository): {id(new_repository)}")
    created_note = note_service.create_note("nice title", "nice content")
    print(f"created note: {created_note}")
    print(f"note_service.list_notes: {note_service.list_notes()}")
