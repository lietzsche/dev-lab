"""P2-2: mappings and sets."""


def find_missing_tags(note, required_tags):
    """Return required tags that are absent from a note."""
    return required_tags - note["tags"]


def run() -> None:
    """Run mapping and set experiments added during P2-2."""
    print()
    print("Run mapping and set experiments added during P2-2.")

    note = {
        "title": "첫 노트",
        "content": "dict 시작",
    }
    print(f"note repr: {repr(note)}")
    print(f"note type: {type(note)}")
    print(f"note length: {len(note)}")
    print(f'note title: {note["title"]}')
    print(f'note content: {note["content"]}')

    note["status"] = "draft"
    for key in note:
        print(f"field: {key} -> {note[key]}")

    note["content"] = "dict 수정"
    for key, value in note.items():
        print(f"updated field: {key} -> {value}")
    
    print(f'title key exists: {"title" in note}')
    print(f'missing key exists: {"missing" in note}')
    print(f'draft key exists: {"draft" in note}')

    missing_value = note.get("missing")
    print(f"missing value: {repr(missing_value)}")
    print(f"missing value is None: {missing_value is None}")

    tag_key = ("metadata", "tags")
    note[tag_key] = ["python", "backend"]
    print(f"metadata tags: {note.get(tag_key)}")
    print(f"tuple key exists: {tag_key in note}")

    tags = {"python", "backend", "python"}
    print(f"tags type: {type(tags)}")
    print(f"tags length: {len(tags)}")
    print(f'python tag exists: {"python" in tags}')
    print(f'llm tag exists: {"llm" in tags}')

    tags.add("python")
    print(f"tags length after duplicate: {len(tags)}")
    tags.add("llm")
    print(f"tags length after new tag: {len(tags)}")
    print(f'llm tag exists after add: {"llm" in tags}')

    requested_tags = {"python", "llm", "mcp"}
    common_tags = tags & requested_tags
    print(f"common tags length: {len(common_tags)}")
    print(f'python is common: {"python" in common_tags}')
    print(f'llm is common: {"llm" in common_tags}')
    print(f'backend is common: {"backend" in common_tags}')
    print(f"common tags is tags: {common_tags is tags}")

    all_tags = tags | requested_tags
    print(f"all tags length: {len(all_tags)}")
    print(f'backend in all tags: {"backend" in all_tags}')
    print(f'mcp in all tags: {"mcp" in all_tags}')
    print(f"all tags is tags: {all_tags is tags}")
    print(f'mcp in original tags: {"mcp" in tags}')

    missing_tags = requested_tags - tags
    extra_tags = tags - requested_tags
    print(f"missing tags length: {len(missing_tags)}")
    print(f'mcp is missing: {"mcp" in missing_tags}')
    print(f"missing tags type: {type(missing_tags)}")
    print(f"extra tags length: {len(extra_tags)}")
    print(f'backend is extra: {"backend" in extra_tags}')

    searchable_note = {
        "title": "검색 노트",
        "tags": {"python", "backend"},
    }
    required_note_tags = {"python", "llm"}
    missing_tags = find_missing_tags(searchable_note, required_note_tags)
    print(f'searchable note title: {searchable_note["title"]}')
    print(f"missing note tags length: {len(missing_tags)}")
    print(f'llm note tag is missing: {"llm" in missing_tags}')
    print(f'original note tags length: {len(searchable_note["tags"])}')
