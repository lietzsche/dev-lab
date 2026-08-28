"""Smoke tests for the initial package scaffold."""

import io
import unittest
from contextlib import redirect_stdout

from knowledge_lab.__main__ import main
from knowledge_lab.lessons import (
    p1_2_names_and_types,
    p1_3_functions_and_scope,
    p1_4_control_flow,
    p2_1_sequences,
    p2_2_mappings_and_sets,
    p2_3_strings_and_bytes,
    p2_4_comprehensions,
)


class MainTest(unittest.TestCase):
    def test_main_prints_note_and_runtime_information(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            main()

        lines = output.getvalue().splitlines()

        self.assertIn("제목: 실제 제목", lines)
        self.assertIn("내용: 실제 내용", lines)
        self.assertIn("제목 repr: '실제 제목'", lines)
        self.assertIn("제목 type: <class 'str'>", lines)
        self.assertIn("내용 type: <class 'str'>", lines)


class NamesAndTypesTest(unittest.TestCase):
    def test_run_prints_rebound_status_and_none(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            p1_2_names_and_types.run()

        lines = output.getvalue().splitlines()

        self.assertIn("status: 원하는 문자열, status type: <class 'str'>", lines)
        self.assertIn("status: 3, status type: <class 'int'>", lines)
        self.assertIn("source: None, source type: <class 'NoneType'>", lines)
        self.assertIn("source is None: True", lines)
        self.assertIn("published: False, published type: <class 'bool'>", lines)
        self.assertIn("published: True, published type: <class 'bool'>", lines)
        self.assertIn("relevance: 1.0, relevance type: <class 'float'>", lines)
        self.assertIn("same_relevance is relevance: True", lines)
        self.assertIn("expected_relevance == actual_relevance: True", lines)
        self.assertIn("expected_relevance is actual_relevance: False", lines)


class FunctionsAndScopeTest(unittest.TestCase):
    def test_remember_title_creates_separate_default_history(self) -> None:
        first_history = p1_3_functions_and_scope.remember_title("First")
        second_history = p1_3_functions_and_scope.remember_title("Second")

        self.assertEqual(["First"], first_history)
        self.assertEqual(["Second"], second_history)
        self.assertIsNot(first_history, second_history)

    def test_functions_return_values_from_arguments(self) -> None:
        self.assertEqual(
            "[TODO] Python 함수",
            p1_3_functions_and_scope.make_note_label(
                title="Python 함수", prefix="TODO"
            ),
        )
        self.assertEqual(2, p1_3_functions_and_scope.increase_note_count(1))


class ControlFlowTest(unittest.TestCase):
    def test_content_state_uses_truthiness(self) -> None:
        self.assertEqual("empty", p1_4_control_flow.content_state(""))
        self.assertEqual("present", p1_4_control_flow.content_state("Python"))

    def test_describe_command_matches_literals_and_alias(self) -> None:
        self.assertEqual("create note", p1_4_control_flow.describe_command("create"))
        self.assertEqual("create note", p1_4_control_flow.describe_command("add"))
        self.assertEqual("search notes", p1_4_control_flow.describe_command("search"))
        self.assertEqual(
            "unknown command", p1_4_control_flow.describe_command("delete")
        )

    def test_find_character_reports_normal_exhaustion(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            p1_4_control_flow.find_character("Lab", "a")
            p1_4_control_flow.find_character("Lab", "z")

        self.assertEqual(["found: a", "not found: z"], output.getvalue().splitlines())


class SequencesTest(unittest.TestCase):
    def test_run_prints_sequence_identity_and_mutability_boundaries(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            p2_1_sequences.run()

        lines = output.getvalue().splitlines()

        self.assertIn("selected titles is note titles: False", lines)
        self.assertIn("selected first is original index 1: True", lines)
        self.assertIn("shared inner tags: True", lines)
        self.assertIn("note summary type: <class 'tuple'>", lines)
        self.assertIn("bundle tags same object: True", lines)
        self.assertIn("remaining titles type: <class 'list'>", lines)
        self.assertIn("head title is original index 0: True", lines)


class MappingsAndSetsTest(unittest.TestCase):
    def test_find_missing_tags_returns_difference_without_mutation(self) -> None:
        note_tags = {"python", "backend"}
        note = {"title": "검색 노트", "tags": note_tags}
        required_tags = {"python", "llm"}

        missing_tags = p2_2_mappings_and_sets.find_missing_tags(
            note, required_tags
        )

        self.assertEqual({"llm"}, missing_tags)
        self.assertEqual({"python", "backend"}, note["tags"])
        self.assertEqual({"python", "llm"}, required_tags)
        self.assertIsNot(missing_tags, note_tags)
        self.assertIsNot(missing_tags, required_tags)

    def test_run_prints_mapping_and_set_boundaries(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            p2_2_mappings_and_sets.run()

        lines = output.getvalue().splitlines()

        self.assertIn("missing value: None", lines)
        self.assertIn("tuple key exists: True", lines)
        self.assertIn("tags length after duplicate: 2", lines)
        self.assertIn("common tags length: 2", lines)
        self.assertIn("mcp in original tags: False", lines)
        self.assertIn("llm note tag is missing: True", lines)
        self.assertIn("original note tags length: 2", lines)


class StringsAndBytesTest(unittest.TestCase):
    def test_parse_note_payload_decodes_valid_utf8(self) -> None:
        payload = "검색 노트|UTF-8 경계".encode("utf-8")

        note = p2_3_strings_and_bytes.parse_note_payload(payload)

        self.assertEqual(
            {"title": "검색 노트", "content": "UTF-8 경계"}, note
        )
        self.assertEqual("검색 노트|UTF-8 경계".encode("utf-8"), payload)

    def test_parse_note_payload_preserves_failure_boundaries(self) -> None:
        self.assertIsNone(
            p2_3_strings_and_bytes.parse_note_payload(
                "구분자 없음".encode("utf-8")
            )
        )

        with self.assertRaises(UnicodeDecodeError):
            p2_3_strings_and_bytes.parse_note_payload(bytes([0xFF]))


class ComprehensionsTest(unittest.TestCase):
    def test_search_note_titles_is_case_insensitive_and_non_mutating(self) -> None:
        notes = [
            {"title": "Python 심화"},
            {"title": "FastAPI with python"},
            {"title": "Rust 기초"},
        ]

        titles = p2_4_comprehensions.search_note_titles(notes, "PYTHON")

        self.assertEqual(["FastAPI with python", "Python 심화"], titles)
        self.assertEqual(
            [
                {"title": "Python 심화"},
                {"title": "FastAPI with python"},
                {"title": "Rust 기초"},
            ],
            notes,
        )
        self.assertIsNot(titles, notes)

    def test_search_note_titles_returns_empty_list_without_match(self) -> None:
        notes = [{"title": "Python"}, {"title": "Rust"}]

        self.assertEqual(
            [], p2_4_comprehensions.search_note_titles(notes, "Java")
        )


if __name__ == "__main__":
    unittest.main()
