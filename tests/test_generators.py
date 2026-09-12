"""Public behavior tests for P5-3 generators."""

import io
import unittest
from contextlib import redirect_stdout

from knowledge_lab.lessons.p3_3_dataclasses_and_value_objects import Note
from knowledge_lab.lessons.p5_3_generators import (
    chain_note_groups,
    stream_note_titles,
)


class GeneratorsTest(unittest.TestCase):
    def test_stream_starts_on_demand_and_stops_at_first_match(self) -> None:
        notes = [
            Note(title="Rust ownership", content="Rust content"),
            Note(title="Python generator", content="Python content"),
            Note(title="Python asyncio", content="Async content"),
        ]
        output = io.StringIO()

        with redirect_stdout(output):
            stream = stream_note_titles(notes, "PYTHON")
            self.assertEqual([], output.getvalue().splitlines())
            first_match = next(stream)

        self.assertEqual("Python generator", first_match)
        self.assertEqual(
            [
                "checking note: Rust ownership",
                "checking note: Python generator",
            ],
            output.getvalue().splitlines(),
        )

    def test_stream_returns_matches_without_mutating_notes(self) -> None:
        notes = [
            Note(title="Python generator", content="Generator content"),
            Note(title="FastAPI", content="API content"),
            Note(title="python asyncio", content="Async content"),
        ]
        original_titles = [note.title for note in notes]

        with redirect_stdout(io.StringIO()):
            matches = list(stream_note_titles(notes, "PYTHON"))

        self.assertEqual(["Python generator", "python asyncio"], matches)
        self.assertEqual(original_titles, [note.title for note in notes])

    def test_yield_from_preserves_group_order(self) -> None:
        with redirect_stdout(io.StringIO()):
            titles = list(
                chain_note_groups(
                    ["Python", "FastAPI"],
                    ["MCP", "LLM"],
                )
            )

        self.assertEqual(["Python", "FastAPI", "MCP", "LLM"], titles)
