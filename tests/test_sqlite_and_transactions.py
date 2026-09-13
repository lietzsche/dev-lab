"""Public behavior tests for P7-3 SQLite and transactions."""

import sqlite3
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from knowledge_lab.lessons.p7_3_sqlite_and_transactions import (
    find_note_by_id,
    init_notes_table,
    insert_note,
    search_notes_by_title,
)


class SqliteAndTransactionsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        init_notes_table(self.connection)

    def tearDown(self) -> None:
        self.connection.close()

    def test_insert_and_find_note_by_id(self) -> None:
        note_id = insert_note(self.connection, "Python", "SQLite persistence")

        self.assertEqual(1, note_id)
        self.assertEqual(
            (1, "Python", "SQLite persistence"),
            find_note_by_id(self.connection, note_id),
        )
        self.assertIsNone(find_note_by_id(self.connection, 999))

    def test_search_notes_by_title_with_safe_parameter_binding(self) -> None:
        insert_note(self.connection, "Python 기초", "내용 1")
        insert_note(self.connection, "Python 심화", "내용 2")
        insert_note(self.connection, "Rust 기초", "내용 3")

        matches = search_notes_by_title(self.connection, "Python")
        self.assertEqual(2, len(matches))
        self.assertEqual("Python 기초", matches[0][1])
        self.assertEqual("Python 심화", matches[1][1])

        # SQL Injection 방어 확인: 악의적 페이로드가 쿼리 구문을 변조하지 않음
        malicious = "Python' OR '1' = '1"
        self.assertEqual([], search_notes_by_title(self.connection, malicious))

    def test_transaction_rolls_back_on_error_and_commits_on_success(self) -> None:
        # 1. 예외 발생 시 자동 롤백
        with self.assertRaises(RuntimeError):
            with self.connection:
                self.connection.execute(
                    "INSERT INTO notes (title, content) VALUES (?, ?)",
                    ("실패할 노트", "에러 예정"),
                )
                raise RuntimeError("강제 실패")

        self.assertEqual([], search_notes_by_title(self.connection, "실패할 노트"))

        # 2. 정상 종료 시 자동 커밋
        valid_id = insert_note(self.connection, "성공한 노트", "커밋 완료")
        self.assertIsNotNone(find_note_by_id(self.connection, valid_id))

    def test_multi_connection_isolation_in_file_database(self) -> None:
        with TemporaryDirectory() as temp_dir:
            db_path = Path(temp_dir) / "test.db"

            setup_conn = sqlite3.connect(db_path)
            init_notes_table(setup_conn)
            setup_conn.close()

            writer_conn = sqlite3.connect(db_path)
            reader_conn = sqlite3.connect(db_path)

            try:
                # writer에서 커밋 전 삽입
                writer_conn.execute(
                    "INSERT INTO notes (title, content) VALUES (?, ?)",
                    ("격리 노트", "커밋 전"),
                )

                # reader에서는 보이지 않음
                reader_cursor = reader_conn.execute(
                    "SELECT id, title FROM notes WHERE title = ?", ("격리 노트",)
                )
                self.assertIsNone(reader_cursor.fetchone())

                # writer 커밋 후
                writer_conn.commit()

                # reader에서도 가시화됨
                reader_cursor = reader_conn.execute(
                    "SELECT id, title FROM notes WHERE title = ?", ("격리 노트",)
                )
                self.assertIsNotNone(reader_cursor.fetchone())
            finally:
                writer_conn.close()
                reader_conn.close()


if __name__ == "__main__":
    unittest.main()
