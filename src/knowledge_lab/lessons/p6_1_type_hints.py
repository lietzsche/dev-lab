"""P6-1: runtime type과 type hint의 역할을 구분한다."""

from typing import Any

from knowledge_lab.lessons.p3_3_dataclasses_and_value_objects import Note, Tag


def repeat_title(title: str, times: int) -> str:
    return title * times


def format_note_id(note_id: int | str) -> str:
    if isinstance(note_id, int):
        return f"note-{note_id}"
    return note_id.strip()


def normalize_source(source: str | None = None) -> str:
    if source is None:
        return "unknown"
    return source.strip()


def normalize_tags(tags: list[str]) -> list[str]:
    return [tag.strip().lower() for tag in tags]


def read_title(payload: Any) -> Any:
    return payload["title"]


def create_note(
    title: str,
    tags: list[str],
    content: str | None = None,
) -> Note:
    title = title.strip()
    if content is None:
        content = ""
    else:
        content = content.strip()
    normalized_tags = [Tag(name=tag) for tag in normalize_tags(tags)]
    return Note(title=title, content=content, tags=normalized_tags)


def run() -> None:
    """Run the current type hint exercise."""
    print()
    print("P6-1 type hint 시작")

    raw_tags = [" Python ", "TYPING"]
    note = create_note(title=" Type hints ", tags=raw_tags)
    print(f"note: {note}")
    print(f"original tags: {raw_tags}")
    print(f"note tag names: {[tag.name for tag in note.tags]}")
