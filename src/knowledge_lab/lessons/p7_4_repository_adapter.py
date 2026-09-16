"""P7-4: repository contract와 adapter 교체 경계를 관찰한다."""

import json
import sqlite3
from pathlib import Path
from tempfile import TemporaryDirectory

from knowledge_lab.lessons.p3_3_dataclasses_and_value_objects import Note, Tag
from knowledge_lab.lessons.p3_4_protocols_and_composition import (
    NoteRepository,
    InMemoryNoteRepository,
)
from knowledge_lab.lessons.p7_2_json_persistence import save_json_atomically
from knowledge_lab.lessons.p7_3_sqlite_and_transactions import (
    init_notes_table,
    insert_note,
)


class JsonNoteRepository:
    def __init__(self, path: Path) -> None:
        self._path: Path = path

    def add(self, note: Note) -> None:
        notes = self.all()
        notes.append(note)
        note_data_list = [note_to_data(note_item) for note_item in notes]
        save_json_atomically(self._path, note_data_list)

    def all(self) -> list[Note]:
        if not self._path.exists():
            return []
        json_text = self._path.read_text(encoding="utf-8")
        note_data_list = json.loads(json_text)
        if not isinstance(note_data_list, list):
            raise ValueError("note file must contain a list")
        return [note_from_data(note_data) for note_data in note_data_list]


class SqliteNoteRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self._connection = connection
        init_notes_table(self._connection)
        migrate_notes_schema(self._connection)

    def add(self, note: Note) -> None:
        tags_json = json.dumps([tag.name for tag in note.tags])
        with self._connection:
            self._connection.execute(
                "insert into notes (title, content, tags_json) values (?, ?, ?)",
                (note.title, note.content, tags_json),
            )

    def all(self) -> list[Note]:
        rows = self._connection.execute(
            "select title, content, tags_json from notes order by id"
        ).fetchall()
        notes: list[Note] = []
        for row in rows:
            if not isinstance(row[2], str):
                raise ValueError("invalid sqlite note row")
            tags_data = json.loads(row[2])
            note = note_from_data(
                {"title": row[0], "content": row[1], "tags": tags_data}
            )
            notes.append(note)
        return notes


def save_and_list_notes(
    repository: NoteRepository,
    note: Note,
) -> list[Note]:
    repository.add(note)
    return repository.all()


def note_to_data(note: Note) -> dict[str, object]:
    return {
        "title": note.title,
        "content": note.content,
        "tags": [tag.name for tag in note.tags],
    }


def note_from_data(data: object) -> Note:
    if not isinstance(data, dict):
        raise ValueError("invalid note data")

    title = data.get("title")
    content = data.get("content")
    tags = data.get("tags")
    if (
        not isinstance(title, str)
        or not isinstance(content, str)
        or not isinstance(tags, list)
    ):
        raise ValueError("invalid note data")
    for tag in tags:
        if not isinstance(tag, str):
            raise ValueError("invalid note data")

    return Note(title=title, content=content, tags=[Tag(name=tag) for tag in tags])


def note_column_names(connection: sqlite3.Connection) -> list[str]:
    rows = connection.execute("pragma table_info(notes)").fetchall()
    return [str(row[1]) for row in rows]


def migrate_notes_schema(connection: sqlite3.Connection) -> None:
    if "tags_json" in note_column_names(connection):
        return
    with connection:
        connection.execute(
            "alter table notes add column tags_json TEXT NOT NULL DEFAULT '[]'"
        )


def run() -> None:
    """Run the current repository adapter exercise."""
    print()
    print("P7-4 repository adapter 시작")

    repository = InMemoryNoteRepository()
    note = Note("Repository", "Adapter boundary")
    notes = save_and_list_notes(repository, note)
    print(f"repository type: {type(repository)}")
    print(f"stored notes: {notes}")
    print(f"stored note is input: {notes[0] is note}")

    tagged_note = Note(
        title="File adapter", content="Mapping boundary", tags=[Tag("python")]
    )
    note_data = note_to_data(tagged_note)
    stored_tags = note_data["tags"]
    print(f"stored tags is list: {isinstance(stored_tags, list)}")
    assert isinstance(stored_tags, list)
    print(f"note data: {note_data}")
    print(f"note data type: {type(note_data)}")
    print(f"data tags is note tags: {note_data['tags'] is tagged_note.tags}")
    print(f"original tag type: {type(tagged_note.tags[0])}")
    print(f"stored tag type: {type(stored_tags[0])}")

    restored_note = note_from_data(note_data)
    print(f"restored note == original: {restored_note == tagged_note}")
    print(f"restored note is original: {restored_note is tagged_note}")
    print(f"restored tags is original tags: {restored_note.tags is tagged_note.tags}")
    print(
        f"restored tag == original tag: {restored_note.tags[0] == tagged_note.tags[0]}"
    )
    print(
        f"restored tag is original tag: {restored_note.tags[0] is tagged_note.tags[0]}"
    )

    with TemporaryDirectory() as context:
        json_path = Path(context) / "notes.json"
        json_repository = JsonNoteRepository(json_path)
        print(f"missing file notes: {json_repository.all()}")
        file_notes = save_and_list_notes(json_repository, tagged_note)
        print(
            f"json repository matches contract: {isinstance(json_repository, NoteRepository)}"
        )
        print(f"file notes: {file_notes}")
        print(f"file note == input: {file_notes[0] == tagged_note}")
        print(f"file note is input: {file_notes[0] is tagged_note}")

    connection = sqlite3.connect(":memory:")
    init_notes_table(connection)

    legacy_note_id = insert_note(connection, "insert title", "insert content")
    print(f"sqlite columns before migration: {note_column_names(connection)}")
    migrate_notes_schema(connection)
    migrate_notes_schema(connection)
    columns_after = note_column_names(connection)
    print(f"sqlite columns after migration: {columns_after}")
    print(f"tags_json column count: {columns_after.count('tags_json')}")
    tags_row = connection.execute(
        "select tags_json from notes where id = ?", (legacy_note_id,)
    ).fetchone()
    assert tags_row is not None
    tags_json = tags_row[0]
    assert isinstance(tags_json, str)
    print(f"legacy tags_json: {json.loads(tags_json)}")

    connection.close()

    sqlite_connection = sqlite3.connect(":memory:")
    sqlite_note = Note("sql title", "sql content", [Tag(name="sql first tags")])
    sqlite_repository = SqliteNoteRepository(sqlite_connection)

    sqlite_notes = save_and_list_notes(sqlite_repository, sqlite_note)

    print(
        f"sqlite repository matches contract: {isinstance(sqlite_repository, NoteRepository)}"
    )
    print(f"sqlite notes: {sqlite_notes}")
    print(f"sqlite note == input: {sqlite_notes[0] == sqlite_note}")
    print(f"sqlite note is input: {sqlite_notes[0] is sqlite_note}")
    print(
        f"sqlite connection usable: {sqlite_connection.execute('select 1').fetchone()}"
    )

    sqlite_connection.close()
