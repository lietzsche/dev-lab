"""P2-4: comprehensions."""


def search_note_titles(note_collection, keyword):
    """Return sorted note titles containing a case-insensitive keyword."""
    normalized_keyword = keyword.lower()
    titles = [
        note["title"]
        for note in note_collection
        if normalized_keyword in note["title"].lower()
    ]
    return sorted(titles)


def get_title_length_after_print_title(title):
    """Print a title and return its length to expose evaluation timing."""
    length = len(title)
    print(f"{title}'s length: {length}")
    return length


def run() -> None:
    """Run comprehension experiments added during P2-4."""
    print()
    print("Run comprehension experiments added during P2-4.")

    notes = ["good_note", "bad_note", "empty_note"]
    note_lens = [len(note) for note in notes]
    print(f"notes: {notes}, repr: {notes!r}, type: {type(notes)}")
    print(f"note_lens: {note_lens}, repr: {note_lens!r}, type: {type(note_lens)}")
    print(f"note_lens is notes: {note_lens is notes}")

    long_notes = [note for note in notes if len(note) >= 9]
    print(f"long notes repr: {long_notes!r}")
    print(f"long notes type: {type(long_notes)}")
    print(f"notes length: {len(notes)}, long_notes length: {len(long_notes)}")

    normalized_long_notes = [note.upper() for note in notes if len(note) >= 9]
    print(f"normalized long notes repr: {normalized_long_notes!r}")
    print(f"notes repr: {notes!r}")

    note_length_by_title = {note: len(note) for note in notes}
    print(f"note_length_by_title repr: {note_length_by_title!r}")
    print(f"note_length_by_title type: {type(note_length_by_title)}")
    print(f"note_length_by_title length: {len(note_length_by_title)}")
    print(f"notes repr: {notes!r}")

    tags = ["Python", "Java", "JS", "python", "llm", "JAVA"]
    normalized_tags = {tag.lower() for tag in tags}
    print(f"normalized_tags repr: {normalized_tags!r}")
    print(f"normalized_tags type: {type(normalized_tags)}")
    print(f"tags length: {len(tags)}")
    print(f"normalized_tags length: {len(normalized_tags)}")
    print(f"python in normalized_tags: {'python' in normalized_tags}")

    generate_length_from_notes = (
        get_title_length_after_print_title(note) for note in notes
    )
    print(f"generate_length_from_notes type: {type(generate_length_from_notes)}")
    print("before next")
    print(f"generate_length_from_notes next: {next(generate_length_from_notes)}")

    remaining_lengths = list(generate_length_from_notes)
    print(f"remaining_lengths repr: {remaining_lengths!r}")
    after_exhaustion = list(generate_length_from_notes)
    print(f"after_exhaustion repr: {after_exhaustion!r}")

    notes_with_tag = [
        {
            "title": "good_note",
            "tags": ["good", "nice"],
        },
        {
            "title": "bad_note",
            "tags": ["bad", "wrong"],
        },
        {
            "title": "python_note",
            "tags": ["python", "not js"],
        },
    ]
    all_normalized_tags = {
        tag.lower() for note in notes_with_tag for tag in note["tags"]
    }
    print(f"all_normalized_tags repr: {all_normalized_tags!r}")
    print(f"all_normalized_tags type: {type(all_normalized_tags)}")
    print(f"all_normalized_tags length: {len(all_normalized_tags)}")
    print(f"python in all_normalized_tags: {'python' in all_normalized_tags}")

    sorted_tags = sorted(all_normalized_tags)
    print(f"sorted_tags repr: {sorted_tags!r}")
    print(f"sorted_tags type: {type(sorted_tags)}")
    print(f"sorted_tags is all_normalized_tags: {sorted_tags is all_normalized_tags}")
    print(f"all_normalized_tags type: {type(all_normalized_tags)}")

    search_notes = [
        {"title": "bad python"},
        {"title": "good python"},
        {"title": "good js"},
    ]
    python_result = search_note_titles(search_notes, "PYTHON")
    java_result = search_note_titles(search_notes, "JAVA")
    print(f"python_result: {python_result}")
    print(f"java_result: {java_result}")
    print(f"search_notes repr: {search_notes!r}")
