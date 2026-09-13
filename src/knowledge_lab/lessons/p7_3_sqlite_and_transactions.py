"""P7-3: SQLite connection, transaction 경계와 parameter binding을 관찰한다."""

import sqlite3
from pathlib import Path
from tempfile import TemporaryDirectory


def init_notes_table(connection: sqlite3.Connection) -> None:
    with connection:
        connection.execute(
            "create table if not exists notes (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, content TEXT NOT NULL)"
        )


def insert_note(connection: sqlite3.Connection, title: str, content: str) -> int:
    with connection:
        cursor = connection.execute(
            "insert into notes (title, content) values (?, ?)", (title, content)
        )
        assert cursor.lastrowid is not None
        return cursor.lastrowid


def find_note_by_id(
    connection: sqlite3.Connection, note_id: int
) -> tuple[int, str, str] | None:
    with connection:
        row = connection.execute(
            "select id, title, content from notes where id = ?", (note_id,)
        ).fetchone()
        if row is None:
            return None
        return (int(row[0]), str(row[1]), str(row[2]))


def search_notes_by_title(
    connection: sqlite3.Connection, title: str
) -> list[tuple[int, str, str]]:
    with connection:
        cursor = connection.execute(
            "select id, title, content from notes where title like ? order by id",
            (f"%{title}%",),
        )
        rows = cursor.fetchall()
        return [(int(row[0]), str(row[1]), str(row[2])) for row in rows]


def run() -> None:
    """Run the current SQLite and transaction exercise."""
    print()
    print("P7-3 SQLite와 transaction 시작")

    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    print(f"connection type: {type(connection)}")
    print(f"cursor type: {type(cursor)}")
    print(f"cursor.connection is connection: {cursor.connection is connection}")

    cursor.execute(
        "create table notes (id INTEGER PRIMARY KEY, title TEXT, content TEXT)"
    )
    cursor.execute(
        "insert into notes (id, title, content) values (1, '첫 번째 노트', 'SQLITE 기초')"
    )
    cursor.execute(
        "insert into notes (id, title, content) values (2, '두 번째 노트', '트랜잭션')"
    )
    cursor.execute("select id, title, content from notes order by id")
    first_row = cursor.fetchone()
    print(f"first row: {first_row}")
    print(f"first row type: {type(first_row)}")
    remaining_rows = cursor.fetchall()
    print(f"remaining row: {remaining_rows}")
    exhausted_row = cursor.fetchone()
    print(f"exhausted row: {exhausted_row}")

    cursor.execute(
        "insert into notes (id, title, content) values (?, ?, ?)",
        (3, "Python's Memory", "객체와 참조"),
    )
    cursor.execute("select id, title, content from notes where id = ?", (3,))
    note_row = cursor.fetchone()
    print(f"bound note row: {note_row}")

    malicious_title = "아무제목' OR '1' = '1"
    cursor.execute(f"select id, title from notes where title = '{malicious_title}'")
    injected_rows = cursor.fetchall()
    print(f"injected rows count: {len(injected_rows)}")
    cursor.execute("select id, title from notes where title = ?", (malicious_title,))
    safe_rows = cursor.fetchall()
    print(f"safe rows count: {len(safe_rows)}")

    connection.commit()
    cursor.execute(
        "insert into notes (id, title, content) values (?, ?, ?)",
        (4, "임시 노트", "롤백 예정"),
    )
    cursor.execute("select id, title from notes where id = ?", (4,))
    print(f"before rollback: {cursor.fetchone()}")
    connection.rollback()
    cursor.execute("select id, title from notes where id = ?", (4,))
    print(f"after rollback: {cursor.fetchone()}")
    cursor.execute("select id, title from notes where id = ?", (1,))
    print(f"commited note: {cursor.fetchone()}")

    try:
        with connection:
            cursor.execute(
                "insert into notes (id, title, content) values (?, ?, ?)",
                (5, "실패할 노트", "에러 발생"),
            )
            raise RuntimeError("트랜잭션 강제 중단")
    except RuntimeError as error:
        print(f"caught transaction error: {error}")
    cursor.execute("select id, title from notes where id = ?", (5,))
    print(f"context rolled back note: {cursor.fetchone()}")
    with connection:
        cursor.execute(
            "insert into notes (id, title, content) values (?, ?, ?)",
            (6, "성공한 노트", "자동 커밋"),
        )
    cursor.execute("select id, title from notes where id = ?", (6,))
    print(f"context commited note: {cursor.fetchone()}")

    connection.close()

    with TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "isolated_notes.db"
        setup_conn = sqlite3.connect(db_path)
        setup_conn.execute(
            "create table notes (id INTEGER PRIMARY KEY, title TEXT, content TEXT)"
        )
        setup_conn.commit()
        setup_conn.close()
        writer_conn = sqlite3.connect(db_path)
        reader_conn = sqlite3.connect(db_path)
        writer_conn.execute(
            "insert into notes (id, title, content) values (?, ?, ?)",
            (10, "격리성 테스트", "커밋 전"),
        )
        row_before = reader_conn.execute(
            "select title, content from notes where id = ?", (10,)
        ).fetchone()
        print(f"reader before commit: {row_before}")
        writer_conn.commit()
        row_after = reader_conn.execute(
            "select title, content from notes where id = ?", (10,)
        ).fetchone()
        print(f"reader after commit: {row_after}")
        writer_conn.close()

        reader_conn.close()
    app_conn = sqlite3.connect(":memory:")
    init_notes_table(app_conn)
    created_id = insert_note(app_conn, "모듈화 노트", "함수로 저장")
    print(f"created note id: {created_id}")

    found_note = find_note_by_id(app_conn, created_id)
    print(f"found note: {found_note}")
    missing_note = find_note_by_id(app_conn, 999)
    print(f"missing note: {missing_note}")

    searched_notes = search_notes_by_title(app_conn, "모듈화")
    print(f"searched notes: {searched_notes}")
    safe_searched_notes = search_notes_by_title(app_conn, "아무제목' OR '1' = '1")
    print(f"safe searched notes: {safe_searched_notes}")

    app_conn.close()
