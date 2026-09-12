"""P6-2: generic과 protocol로 type 관계와 동작 계약을 표현한다."""

from typing import Callable, Generic, Protocol, TypeVar, runtime_checkable

from knowledge_lab.lessons.p3_3_dataclasses_and_value_objects import Note


T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


class ItemBox(Generic[T]):
    def __init__(self, item: T) -> None:
        self.item = item

    def get(self) -> T:
        return self.item


class MemoryRepository(Generic[T]):
    def __init__(self) -> None:
        self._items: dict[int, T] = {}

    def save(self, key: int, item: T) -> None:
        self._items[key] = item

    def get(self, key: int) -> T:
        return self._items[key]


class BrokenRepository:
    def save(self) -> None:
        return None

    def get(self) -> int:
        return 0


@runtime_checkable
class Repository(Protocol[T]):
    def save(self, key: int, item: T) -> None: ...

    def get(self, key: int) -> T: ...


def load_item(repository: Repository[T], key: int) -> T:
    return repository.get(key)


def apply_formatter(
    value: T,
    formatter: Callable[[T], str],
) -> str:
    return formatter(value)


def format_title(title: str) -> str:
    return title.upper()


def format_count(count: int) -> str:
    return f"{count} notes"


def format_note(note: Note) -> str:
    return f"{note.title}: {note.content}"


def load_and_format(
    repository: Repository[Note],
    key: int,
    formatter: Callable[[Note], str],
) -> str:
    note = load_item(repository, key)
    return formatter(note)


def run() -> None:
    """Run the current generic and protocol exercise."""
    print()
    print("P6-2 generic과 protocol 시작")

    repository = MemoryRepository[Note]()
    note = Note(title="Python typing", content="Generic repository")
    repository.save(1, note)
    note_label = load_and_format(repository, 1, format_note)
    print(f"note label: {note_label}")
    print(f"same note object: {repository.get(1) is note}")
