"""Public behavior tests for P7-1 path and file I/O."""

from pathlib import Path

from knowledge_lab.lessons.p7_1_paths_and_file_io import (
    NoteRecord,
    read_note_bytes,
    read_note_text,
    serialize_note,
    write_note_bytes,
    write_note_text,
)


def test_text_io_round_trip_preserves_unicode(tmp_path: Path) -> None:
    path = tmp_path / "note.txt"
    content = "Python 파일"

    written_count = write_note_text(path, content)

    assert written_count == len(content)
    assert read_note_text(path) == content
    assert path.read_bytes() == content.encode("utf-8")


def test_binary_io_round_trip_preserves_bytes(tmp_path: Path) -> None:
    path = tmp_path / "note.bin"
    payload = "Python 파일".encode("utf-8")

    written_count = write_note_bytes(path, payload)

    assert written_count == len(payload)
    assert read_note_bytes(path) == payload


def test_serialization_is_separate_from_file_io(tmp_path: Path) -> None:
    note = NoteRecord(title="File I/O", content="Persistence boundary")
    path = tmp_path / "serialized-note.txt"

    serialized_note = serialize_note(note)
    write_note_text(path, serialized_note)

    assert serialized_note == "File I/O\nPersistence boundary"
    assert read_note_text(path) == serialized_note
    assert note == NoteRecord(title="File I/O", content="Persistence boundary")
