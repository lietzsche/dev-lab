"""Public behavior tests for P7-2 JSON persistence."""

import json
from pathlib import Path

import pytest

from knowledge_lab.lessons.p7_2_json_persistence import (
    migrate_note_to_v2,
    read_schema_version,
    require_note_object,
    require_note_title,
    save_json_atomically,
)


def test_note_validation_narrows_json_data() -> None:
    data: object = {"title": "Python"}

    note = require_note_object(data)

    assert note is data
    assert require_note_title(note) == "Python"


@pytest.mark.parametrize("data", [None, [], "note"])
def test_note_object_rejects_non_mapping_json_values(data: object) -> None:
    with pytest.raises(ValueError, match="note data must be a JSON object"):
        require_note_object(data)


@pytest.mark.parametrize("title", [None, 42, ["Python"]])
def test_note_title_rejects_missing_or_non_string_values(title: object) -> None:
    data = {} if title is None else {"title": title}

    with pytest.raises(ValueError, match="note title must be a string"):
        require_note_title(data)


def test_schema_version_defaults_without_mutating_legacy_data() -> None:
    legacy = {"title": "Legacy"}

    version = read_schema_version(legacy)

    assert version == 1
    assert "schema_version" not in legacy


@pytest.mark.parametrize("version", [True, "2", 2.0])
def test_schema_version_rejects_non_integer_json_types(version: object) -> None:
    with pytest.raises(ValueError, match="schema version must be an integer"):
        read_schema_version({"schema_version": version})


def test_migration_creates_v2_data_without_mutating_legacy_data() -> None:
    legacy = {"title": "Legacy"}

    migrated = migrate_note_to_v2(legacy)

    assert migrated == {
        "title": "Legacy",
        "schema_version": 2,
        "source": "unknown",
    }
    assert migrated is not legacy
    assert legacy == {"title": "Legacy"}


def test_atomic_save_replaces_target_with_complete_json(tmp_path: Path) -> None:
    path = tmp_path / "note.json"
    path.write_text('{"title": "Stable"}', encoding="utf-8")

    save_json_atomically(path, {"title": "파이썬 JSON"})

    assert json.loads(path.read_text(encoding="utf-8")) == {"title": "파이썬 JSON"}
    assert not path.with_name(path.name + ".tmp").exists()


def test_atomic_save_preserves_target_when_serialization_fails(tmp_path: Path) -> None:
    path = tmp_path / "note.json"
    stable_text = '{"title": "Stable"}'
    path.write_text(stable_text, encoding="utf-8")

    with pytest.raises(TypeError, match="not JSON serializable"):
        save_json_atomically(path, {"tags": {"python"}})

    assert path.read_text(encoding="utf-8") == stable_text
    assert not path.with_name(path.name + ".tmp").exists()
