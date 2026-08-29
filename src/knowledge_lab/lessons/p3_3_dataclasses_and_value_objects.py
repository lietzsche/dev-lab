"""P3-3: dataclasses and value objects."""

from dataclasses import dataclass, field


@dataclass
class NoteDraft:
    title: str
    content: str


@dataclass(frozen=True)
class Tag:
    name: str

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("tag name must not be blank")


@dataclass(frozen=True)
class FrozenNote:
    tags: list[str]


@dataclass(slots=True)
class SlottedNote:
    title: str


@dataclass
class Note:
    title: str
    content: str
    tags: list[Tag] = field(default_factory=list)

    def add_tag(self, tag: Tag) -> None:
        if tag not in self.tags:
            self.tags.append(tag)


def run() -> None:
    """Run dataclass and value object experiments added during P3-3."""
    print()
    print("Run dataclass and value object experiments added during P3-3.")

    note_draft = NoteDraft(title="good title", content="bad content")
    print(f"note_draft repr: {note_draft!r}")
    print(f"note_draft type: {type(note_draft)}")
    print(f"note_draft __dict__: {note_draft.__dict__}")
    print(f"note_draft title: {note_draft.title}")
    print(f"note_draft content: {note_draft.content}")

    same_draft = NoteDraft(title="good title", content="bad content")
    different_draft = NoteDraft(title="good title", content="good content")
    print(f"note_draft is same_draft: {note_draft is same_draft}")
    print(f"note_draft == same_draft: {note_draft == same_draft}")
    print(f"note_draft == different_draft: {note_draft == different_draft}")

    good_tag = Tag(name="first good")
    print(f"good tag - repr: {good_tag!r}, - name: {good_tag.name}")
    # good_tag.name = "second good"  # FrozenInstanceError 관찰 완료

    frozen_note = FrozenNote(["ice"])
    frozen_note.tags.append("fire")
    print(f"frozen note's tags: {frozen_note.tags}")

    slotted_note = SlottedNote("slot title")
    print(f"slotted_note repr: {slotted_note!r}")
    print(f"slotted_note title: {slotted_note.title}")
    print(
        "slotted_note hasattr __dict__: "
        f"{hasattr(slotted_note, '__dict__')}"
    )
    # slotted_note.content = "add content"  # AttributeError 관찰 완료

    bad_draft_note = NoteDraft(title=1990, content=None)
    print(f"bad draft note repr: {bad_draft_note!r}")
    print(f"bad draft note title type: {type(bad_draft_note.title)}")
    print(f"bad draft note content type: {type(bad_draft_note.content)}")

    # blank_tag = Tag(" ")  # ValueError validation 관찰 완료

    nice_first_note = Note(title="1 note", content="1")
    nice_second_note = Note(title="2 note", content="2")
    print(
        "nice first note's tags is nice second note's tags: "
        f"{nice_first_note.tags is nice_second_note.tags}"
    )
    nice_first_note.tags.append(Tag(name="python"))
    print(f"nice first note repr: {nice_first_note!r}")
    print(f"nice second note repr: {nice_second_note!r}")
    print(f"nice first note tags: {nice_first_note.tags}")
    print(f"nice second note tags: {nice_second_note.tags}")

    nice_tag = Tag(name="nice")
    nice_same_tag = Tag(name="nice")
    print(f"nice tag is nice same tag: {nice_tag is nice_same_tag}")
    print(f"nice tag == nice same tag: {nice_tag == nice_same_tag}")
    some_note = Note(title="some title", content="some content")
    some_note.add_tag(nice_tag)
    some_note.add_tag(nice_same_tag)
    print(f"some_note tags: {some_note.tags}")
