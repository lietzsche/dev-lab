"""P3-1: mutability, aliasing, and copy."""
from copy import deepcopy


def run() -> None:
    """Run mutability, aliasing, and copy experiments added during P3-1."""
    print()
    print("Run mutability, aliasing, and copy experiments added during P3-1.")

    original_tags = ["python", "backend"]
    shared_tags = original_tags
    shared_tags.append("java")
    print(f"original_tags: {original_tags!r}")
    print(f"shared_tags: {shared_tags!r}")
    print(f"original_tags is shared_tags: {original_tags is shared_tags}")
    print(f"original_tags id: {id(original_tags)}")
    print(f"shared_tags id: {id(shared_tags)}")

    rebound_tags = original_tags
    rebound_tags = ["typescript"]
    print(f"original_tags : {original_tags!r}")
    print(f"rebound_tags : {rebound_tags!r}")
    print(f"rebound_tags is original_tags: {rebound_tags is original_tags}")

    original_note_groups = [["A"], ["B"]]
    copied_note_groups = original_note_groups.copy()
    print(
        "original_note_groups is copied_note_groups: "
        f"{original_note_groups is copied_note_groups}"
    )
    print(
        "original_note_groups[0] is copied_note_groups[0]: "
        f"{original_note_groups[0] is copied_note_groups[0]}"
    )
    copied_note_groups[0].append("C")
    print(f"original_note_groups: {original_note_groups}")
    print(f"copied_note_groups: {copied_note_groups}")

    original_sections = [[1, 2, 3], ["a", "b", "c"], ["가", "나", "다"]]
    deep_copied_sections = deepcopy(original_sections)
    print(
        "original_sections is deep_copied_sections: "
        f"{original_sections is deep_copied_sections}"
    )
    print(
        "original_sections[0] is deep_copied_sections[0]: "
        f"{original_sections[0] is deep_copied_sections[0]}"
    )
    deep_copied_sections[0].append(4)
    deep_copied_sections[0].append(5)
    deep_copied_sections[0].append(6)
    print(f"original_sections: {original_sections!r}")
    print(f"deep_copied_sections: {deep_copied_sections!r}")

    caller_tags = ["call", "tags"]
    append_function(caller_tags)
    print(f"caller_tags id: {id(caller_tags)}")
    print(f"caller_tags: {caller_tags!r}")
    change_new_list(caller_tags)
    print(f"caller_tags: {caller_tags!r}")

    note = {
        "title": "Python 객체 모델",
        "tags": ["python", "object"],
    }
    copied_note = copy_note(note)
    copied_note["tags"].append("copy")
    print(f"note is copied note: {note is copied_note}")
    print(
        "note tags is copied note tags: "
        f"{note['tags'] is copied_note['tags']}"
    )
    print(f"note tags: {note['tags']}")
    print(f"copied_note tags: {copied_note['tags']}")


def append_function(args):
    """Append a tag through a shared parameter."""
    args.append("function")
    print(f"args id: {id(args)}")


def change_new_list(args):
    """Rebind a parameter to a new list and return it."""
    args = ["new", "change"]
    return args


def copy_note(note):
    """Return a note whose outer dict and tags list are independent copies."""
    new_note = note.copy()
    new_note["tags"] = note["tags"].copy()
    return new_note
