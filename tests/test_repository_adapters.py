"""Public behavior tests for P7-4 repository adapters."""

import sqlite3
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from knowledge_lab.lessons.p3_3_dataclasses_and_value_objects import Note, Tag
from knowledge_lab.lessons.p3_4_protocols_and_composition import NoteRepository
from knowledge_lab.lessons.p7_3_sqlite_and_transactions import (
    init_notes_table,
    insert_note,
)
from knowledge_lab.lessons.p7_4_repository_adapter import (
    JsonNoteRepository,
    SqliteNoteRepository,
    migrate_notes_schema,
    note_column_names,
    note_from_data,
    note_to_data,
    save_and_list_notes,
)


class NoteMappingTest(unittest.TestCase):
    def test_note_round_trip_preserves_value_with_fresh_objects(self) -> None:
        original = Note("Mapping", "Persistence boundary", [Tag("python")])

        data = note_to_data(original)
        restored = note_from_data(data)

        self.assertEqual(original, restored)
        self.assertIsNot(original, restored)
        self.assertIsNot(original.tags, restored.tags)
        self.assertIsNot(original.tags[0], restored.tags[0])
        self.assertIsNot(original.tags, data["tags"])

    def test_note_from_data_rejects_invalid_persistence_shape(self) -> None:
        invalid_values = [
            ["not", "an", "object"],
            {"title": 42, "content": "content", "tags": []},
            {"title": "title", "content": "content", "tags": [42]},
        ]

        for invalid_value in invalid_values:
            with self.subTest(value=invalid_value):
                with self.assertRaises(ValueError):
                    note_from_data(invalid_value)


class JsonNoteRepositoryTest(unittest.TestCase):
    def test_missing_file_is_empty_and_saved_note_survives_new_adapter(self) -> None:
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "notes.json"
            repository = JsonNoteRepository(path)
            note = Note("JSON", "File adapter", [Tag("json")])

            self.assertEqual([], repository.all())
            saved_notes = save_and_list_notes(repository, note)
            reloaded_notes = JsonNoteRepository(path).all()

            self.assertIsInstance(repository, NoteRepository)
            self.assertEqual([note], saved_notes)
            self.assertEqual([note], reloaded_notes)
            self.assertIsNot(note, reloaded_notes[0])


class SqliteNoteRepositoryTest(unittest.TestCase):
    def test_migration_is_idempotent_and_preserves_legacy_row(self) -> None:
        connection = sqlite3.connect(":memory:")
        try:
            init_notes_table(connection)
            note_id = insert_note(connection, "Legacy", "Before migration")

            migrate_notes_schema(connection)
            migrate_notes_schema(connection)

            columns = note_column_names(connection)
            tags_row = connection.execute(
                "select tags_json from notes where id = ?", (note_id,)
            ).fetchone()
            self.assertEqual(1, columns.count("tags_json"))
            self.assertEqual(("[]",), tags_row)
        finally:
            connection.close()

    def test_saved_note_survives_reconnection_as_fresh_domain_object(self) -> None:
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "notes.db"
            note = Note("SQLite", "Database adapter", [Tag("sqlite")])

            writer = sqlite3.connect(path)
            try:
                repository = SqliteNoteRepository(writer)
                save_and_list_notes(repository, note)
                self.assertIsInstance(repository, NoteRepository)
                self.assertEqual((1,), writer.execute("select 1").fetchone())
            finally:
                writer.close()

            reader = sqlite3.connect(path)
            try:
                reloaded_notes = SqliteNoteRepository(reader).all()
            finally:
                reader.close()

            self.assertEqual([note], reloaded_notes)
            self.assertIsNot(note, reloaded_notes[0])
            self.assertIsNot(note.tags, reloaded_notes[0].tags)


if __name__ == "__main__":
    unittest.main()
