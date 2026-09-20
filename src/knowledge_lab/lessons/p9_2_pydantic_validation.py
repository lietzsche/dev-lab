"""P9-2: Pydantic transport schema의 validation 경계를 관찰한다."""

from pydantic import BaseModel, Field

from knowledge_lab.lessons.p3_3_dataclasses_and_value_objects import Note, Tag


class NoteCreatePayload(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str
    tags: list[str]


def to_domain_note(payload: NoteCreatePayload) -> Note:
    return Note(
        title=payload.title,
        content=payload.content,
        tags=[Tag(name=tag) for tag in payload.tags],
    )


def run() -> None:
    """Run the current Pydantic validation exercise."""
    print()
    print("P9-2 Pydantic validation 시작")

    raw_payload: dict[str, object] = {
        "title": "Pydantic boundary",
        "content": "Transport to domain",
        "tags": ["python", "pydantic"],
    }
    payload = NoteCreatePayload.model_validate(raw_payload)
    domain_note = to_domain_note(payload)
    print(f"payload repr: {payload!r}")
    print(f"payload type: {type(payload)}")
    print(f"domain_note repr: {domain_note!r}")
    print(f"domain_note type: {type(domain_note)}")
    print(f"payload first tags type: {type(payload.tags[0])}")
    print(f"domain note first tags type: {type(domain_note.tags[0])}")
    print(f"payload title == domain note title: {payload.title == domain_note.title}")
    print(f"payload tags id: {id(payload.tags)}")
    print(f"domain note tags id: {id(domain_note.tags)}")
    print(f"tags identity equal: {id(payload.tags) == id(domain_note.tags)}")
