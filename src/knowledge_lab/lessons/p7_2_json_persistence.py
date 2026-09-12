"""P7-2: JSON serialization과 persistence 실패 경계를 관찰한다."""

import json
from pathlib import Path
from tempfile import TemporaryDirectory


def require_note_object(data: object) -> dict[str, object]:
    if not isinstance(data, dict):
        raise ValueError("note data must be a JSON object")
    return data


def require_note_title(data: dict[str, object]) -> str:
    title = data.get("title")
    if not isinstance(title, str):
        raise ValueError("note title must be a string")
    return title


def read_schema_version(data: dict[str, object]) -> int:
    schema_version = data.get("schema_version", 1)
    if type(schema_version) is not int:
        raise ValueError("schema version must be an integer")
    return schema_version


def migrate_note_to_v2(data: dict[str, object]) -> dict[str, object]:
    new_data = data.copy()
    new_data["schema_version"] = 2
    new_data["source"] = "unknown"
    return new_data


def save_json_atomically(path: Path, data: object) -> None:
    text = json.dumps(data, ensure_ascii=False)
    tmp_path = path.with_name(path.name + ".tmp")
    tmp_path.write_text(text, encoding="utf-8")
    tmp_path.replace(path)


def run() -> None:
    """Run the current JSON persistence exercise."""
    print()
    print("P7-2 JSON persistence 시작")

    note_data = {
        "title": "파이썬 JSON",
        "tags": ("python", "json"),
        "published": False,
        "source": None,
    }
    json_text = json.dumps(note_data, ensure_ascii=False)
    restored_data = json.loads(json_text)
    print(f"json text repr: {json_text!r}")
    print(f"json text type: {type(json_text)}")
    print(f"restored data repr: {restored_data!r}")
    print(f"restored data type: {type(restored_data)}")
    print(f"note data tags type: {type(note_data['tags'])}")
    print(f"restored data tags type: {type(restored_data['tags'])}")
    print(f"note data == restored data: {note_data == restored_data}")

    with TemporaryDirectory() as context:
        tmp_dir_path = Path(context)
        note_json_path = tmp_dir_path / "note.json"
        with note_json_path.open("w", encoding="utf-8") as writer:
            json.dump(note_data, writer, ensure_ascii=False)
            print(f"[in block] writer.closed: {writer.closed}")
        print(f"[after block] writer.closed: {writer.closed}")
        with note_json_path.open("r", encoding="utf-8") as reader:
            loaded_from_file = json.load(reader)
            print(f"[in block] reader.closed: {reader.closed}")
        print(f"[after block] reader.closed: {reader.closed}")
        print(f"loaded from file repr: {loaded_from_file!r}")
        print(f"loaded from file type: {type(loaded_from_file)}")
        print(f"loaded from file == note data: {loaded_from_file == note_data}")
        print(f"loaded from file == restored data: {loaded_from_file == restored_data}")

        broken_json_path = tmp_dir_path / "broken.json"
        broken_json_data = '{"title": "broken"'
        broken_json_path.write_text(broken_json_data, encoding="utf-8")
        try:
            with broken_json_path.open("r", encoding="utf-8") as reader:
                json.load(reader)
        except json.JSONDecodeError as error:
            print(f"error type: {type(error)}")
            print(f"error msg: {error.msg}")
            print(f"error lineno: {error.lineno}")
            print(f"error colno: {error.colno}")
            print(f"error pos: {error.pos}")
            print(f"broken reader.closed: {reader.closed}")

    dumped_data = json.dumps(["Python", "JSON"])
    json_data = json.loads(dumped_data)
    print(f"json data repr: {json_data!r}")
    print(f"json data type: {type(json_data)}")

    try:
        require_note_object(json_data)
    except ValueError as error:
        print(f"error type: {type(error)}")
        print(f"error message: {error}")

    title_number = '{"title": 42}'
    title_str = '{"title": "Python"}'
    try:
        parsed_data = json.loads(title_number)
        note_object = require_note_object(parsed_data)
        title = require_note_title(note_object)
        print(f"title number result: {title}")
    except ValueError as error:
        print(f"error: {error}")
    try:
        parsed_data = json.loads(title_str)
        note_object = require_note_object(parsed_data)
        title = require_note_title(note_object)
        print(f"title str result: {title}")
    except ValueError as error:
        print(f"error: {error}")

    legacy_json_text = '{"title":"Legacy"}'
    legacy_data = json.loads(legacy_json_text)
    legacy_object = require_note_object(legacy_data)
    legacy_version = read_schema_version(legacy_object)
    print(f"legacy version: {legacy_version}")
    current_json_text = '{"schema_version":2, "title":"Current"}'
    current_data = json.loads(current_json_text)
    current_object = require_note_object(current_data)
    current_version = read_schema_version(current_object)
    print(f"current version: {current_version}")
    print(f"legacy has schema_version: {'schema_version' in legacy_object}")

    migrated_object = migrate_note_to_v2(legacy_object)
    print(f"migrated version: {migrated_object['schema_version']}")
    print(f"migrated source: {migrated_object['source']}")
    print(f"migrated is legacy: {migrated_object is legacy_object}")
    print(f"legacy has schema_version: {'schema_version' in legacy_object}")
    print(f"legacy has source: {'source' in legacy_object}")

    with TemporaryDirectory() as partial_context:
        tmp_dir_path = Path(partial_context)
        data_path = tmp_dir_path / "partial.json"
        stable_json_text = json.dumps({"title": "Stable"})
        data_path.write_text(stable_json_text, encoding="utf-8")
        try:
            with data_path.open("w", encoding="utf-8") as writer:
                json.dump({"title": "New", "tags": {"Python"}}, writer)
        except TypeError as error:
            print(f"error type: {type(error)}")
            print(f"error message: {error}")
        text = data_path.read_text(encoding="utf-8")
        print(f"text repr: {text!r}")
        print(f"text == stable_json_text: {text == stable_json_text}")
        try:
            json.loads(text)
        except json.JSONDecodeError as error:
            print(f"error: {error}")

        data_path.write_text(stable_json_text, encoding="utf-8")
        try:
            unstable_json_text = json.dumps({"title": "New", "tags": {"Python"}})
            data_path.write_text(unstable_json_text, encoding="utf-8")
        except TypeError as error:
            print(f"serialize first error: {error}")
        preserved_text = data_path.read_text(encoding="utf-8")
        print(f"stable text preserved: {stable_json_text == preserved_text}")

    with TemporaryDirectory() as atomic_context:
        atomic_dir_path = Path(atomic_context)
        atomic_path = atomic_dir_path / "target.json"
        atomic_path.write_text(json.dumps({"title": "Stable"}), encoding="utf-8")
        save_json_atomically(atomic_path, {"title": "Atomic"})
        saved_json_text = atomic_path.read_text(encoding="utf-8")
        print(f"atomic title: {json.loads(saved_json_text)['title']}")
        atomic_temporary_path = atomic_dir_path / "target.json.tmp"
        print(f"atomic temporary exists: {atomic_temporary_path.exists()}")
        try:
            save_json_atomically(atomic_path, {"bad set": {"bad", "set"}})
        except TypeError as error:
            print(f"atomic serialize error: {error}")
        preserved_json_text = atomic_path.read_text(encoding="utf-8")
        print(f"atomic title preserved: {json.loads(preserved_json_text)['title']}")

    try:
        read_schema_version({"schema_version": "bad"})
    except ValueError as error:
        print(f"schema version error: {error}")
