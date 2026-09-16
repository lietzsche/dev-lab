"""Public behavior tests for P8-3 coroutines and the event loop."""

import asyncio
import inspect
import io
import unittest
from contextlib import redirect_stdout
from collections.abc import Callable
from unittest.mock import patch

from knowledge_lab.lessons.p8_3_coroutines_and_event_loop import (
    build_note_label,
    load_sources_concurrently,
    load_sources_sequentially,
    load_sources_with_to_thread,
    make_note_title,
    run_note_task,
)


class CoroutinesAndEventLoopTest(unittest.TestCase):
    def test_async_call_creates_an_unstarted_coroutine(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            coroutine = make_note_title("Python docs")

        self.assertTrue(inspect.iscoroutine(coroutine))
        self.assertEqual("", output.getvalue())
        coroutine.close()

    def test_await_connects_nested_coroutine_result(self) -> None:
        with redirect_stdout(io.StringIO()):
            result = asyncio.run(build_note_label("Python docs"))

        self.assertEqual("Note: Python docs", result)

    def test_task_owns_pending_and_completed_state(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            result = asyncio.run(run_note_task())

        self.assertEqual("Note: Python docs", result)
        self.assertIn("task name: note-label, task done: False", output.getvalue())
        self.assertIn("task name: note-label, task done: True", output.getvalue())

    def test_sequential_loader_preserves_source_order(self) -> None:
        sources = ["Python docs", "SQLite docs"]

        with redirect_stdout(io.StringIO()):
            results = asyncio.run(load_sources_sequentially(sources, 0))

        self.assertEqual(sources, results)
        self.assertIsNot(sources, results)

    def test_concurrent_loader_starts_all_tasks_before_completion(self) -> None:
        sources = ["Python docs", "SQLite docs"]
        started: list[str] = []

        async def scenario() -> list[str]:
            both_started = asyncio.Event()

            async def controlled_load(source: str, _: float) -> str:
                started.append(source)
                if len(started) == len(sources):
                    both_started.set()
                await asyncio.wait_for(both_started.wait(), timeout=1)
                return source

            with patch(
                "knowledge_lab.lessons.p8_3_coroutines_and_event_loop.load_note_source",
                new=controlled_load,
            ):
                return await load_sources_concurrently(sources, 0)

        results = asyncio.run(scenario())

        self.assertEqual(sources, started)
        self.assertEqual(sources, results)

    def test_blocking_calls_are_scheduled_through_to_thread(self) -> None:
        sources = ["Python docs", "SQLite docs"]
        started: list[str] = []

        async def controlled_to_thread(
            _: Callable[[str, float], str],
            source: str,
            __: float,
        ) -> str:
            started.append(source)
            if len(started) == len(sources):
                return source
            await asyncio.sleep(0)
            return source

        with patch(
            "knowledge_lab.lessons.p8_3_coroutines_and_event_loop.asyncio.to_thread",
            new=controlled_to_thread,
        ):
            results = asyncio.run(load_sources_with_to_thread(sources, 0))

        self.assertEqual(sources, started)
        self.assertEqual(sources, results)


if __name__ == "__main__":
    unittest.main()
