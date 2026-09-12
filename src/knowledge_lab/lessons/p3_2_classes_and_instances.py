"""P3-2: classes and instances."""


class Note:
    kind = "nice note"
    shared_tags = []

    def __init__(self, title):
        self.title = title
        self.tags = []

    def rename(self, new_title):
        print(f"id: {id(self)}")
        self.title = new_title

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)


def run() -> None:
    """Run class and instance experiments added during P3-2."""
    print()
    print("Run class and instance experiments added during P3-2.")

    first_note = Note("first title")
    second_note = Note("second title")
    print(
        f"first_note: repr - {first_note!r}, "
        f"\ntype - {type(first_note)}, \nid - {id(first_note)}"
    )
    print(
        f"second_note: repr - {second_note!r}, "
        f"\ntype - {type(second_note)}, \nid - {id(second_note)}"
    )
    print(f"first_note is second_note: {first_note is second_note}")
    print(f"type(first_note) is Note: {type(first_note) is Note}")
    print(f"type(second_note) is Note: {type(second_note) is Note}")

    print(f"first note dict: {first_note.__dict__}")
    print(f"second note dict: {second_note.__dict__}")
    first_note.title = "first read"
    print(f"first note dict: {first_note.__dict__}")
    print(f"second note dict: {second_note.__dict__}")

    print(f"Note kind: {Note.kind}")
    print(f"first_note.kind: {first_note.kind}")
    print(f"second_note.kind: {second_note.kind}")
    print(f"first_note dict: {first_note.__dict__}")
    print(f"second_note dict: {second_note.__dict__}")
    first_note.kind = "good note"
    print(f"Note kind: {Note.kind}")
    print(f"first_note.kind: {first_note.kind}")
    print(f"second_note.kind: {second_note.kind}")
    print(f"first_note dict: {first_note.__dict__}")
    print(f"second_note dict: {second_note.__dict__}")

    first_note.shared_tags.append("first tags")
    print(f"Note.shared_tags: {Note.shared_tags}")
    print(f"first_note.shared_tags: {first_note.shared_tags}")
    print(f"second_note.shared_tags: {second_note.shared_tags}")
    print(
        "Note.shared_tags is first_note.shared_tags: "
        f"{Note.shared_tags is first_note.shared_tags}"
    )
    print(
        "Note.shared_tags is second_note.shared_tags: "
        f"{Note.shared_tags is second_note.shared_tags}"
    )
    print(
        "first_note.shared_tags is second_note.shared_tags: "
        f"{first_note.shared_tags is second_note.shared_tags}"
    )
    print(f"first_note dict: {first_note.__dict__}")
    print(f"second_note dict: {second_note.__dict__}")

    print(f"first note id: {id(first_note)}")
    first_note.rename("new first note")
    print(f"first_note.title: {first_note.title}")
    print(f"second_note.title: {second_note.title}")

    print(f"Note.rename - repr: {Note.rename!r}, type: {type(Note.rename)}")
    print(
        "first_note.rename - "
        f"repr: {first_note.rename!r}, type: {type(first_note.rename)}"
    )
    print(
        "first_note.rename.__self__ is first_note: "
        f"{first_note.rename.__self__ is first_note}"
    )
    print(
        "first_note.rename.__func__ is Note.rename: "
        f"{first_note.rename.__func__ is Note.rename}"
    )
    print(f"before second_note.title: {second_note.title}")
    Note.rename(second_note, "new second note title")
    print(f"after second_note.title: {second_note.title}")

    print(f"first note tags is second note tags: {first_note.tags is second_note.tags}")
    first_note.tags.append("first tags")
    print(f"first_note tags: {first_note.tags}")
    print(f"second_note tags: {second_note.tags}")

    good_note = Note("good")
    bad_note = Note("bad")
    good_note.add_tag("nice")
    good_note.add_tag("python")
    good_note.add_tag("nice")
    print(f"good_note tags: {good_note.tags}")
    print(f"bad_note tags: {bad_note.tags}")
