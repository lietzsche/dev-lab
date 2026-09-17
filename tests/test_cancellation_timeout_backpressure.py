"""Public behavior tests for P8-4 cancellation and backpressure."""

import asyncio
import io
import unittest
from contextlib import redirect_stdout

from knowledge_lab.lessons.p8_4_cancellation_timeout_backpressure import (
    import_note_source_with_cleanup,
    observe_manual_cancellation,
    observe_queue_completion,
    observe_task_group_failure,
    run_note_import_pipeline,
)


class CancellationTimeoutBackpressureTest(unittest.TestCase):
    def test_task_group_failure_cancels_its_sibling(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            asyncio.run(observe_task_group_failure())

        self.assertIn("error group exceptions length: 1", output.getvalue())
        self.assertIn("fail task done: True", output.getvalue())
        self.assertIn("slow task cancelled: True", output.getvalue())

    def test_manual_cancellation_reaches_the_awaiting_owner(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            asyncio.run(observe_manual_cancellation())

        self.assertIn("return cancel: True", output.getvalue())
        self.assertIn("task done: True", output.getvalue())
        self.assertIn("task cancelled: True", output.getvalue())

    def test_cancelled_import_cleans_up_and_propagates(self) -> None:
        output = io.StringIO()

        async def scenario() -> asyncio.Task[str]:
            task = asyncio.create_task(
                import_note_source_with_cleanup("Cleanup docs", 10)
            )
            await asyncio.sleep(0)
            task.cancel()
            with self.assertRaises(asyncio.CancelledError):
                await task
            return task

        with redirect_stdout(output):
            task = asyncio.run(scenario())

        self.assertTrue(task.cancelled())
        self.assertIn("cancel received: Cleanup docs", output.getvalue())
        self.assertIn("cleanup: Cleanup docs", output.getvalue())
        self.assertNotIn("import end: Cleanup docs", output.getvalue())

    def test_queue_join_waits_for_every_task_done_signal(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            asyncio.run(observe_queue_completion())

        self.assertIn("queue size: 0", output.getvalue())
        self.assertIn("join task done: False", output.getvalue())
        self.assertTrue(output.getvalue().endswith("join task done: True\n"))

    def test_bounded_pipeline_preserves_source_order(self) -> None:
        sources = ["Python docs", "SQLite docs", "AsyncIO docs"]

        with redirect_stdout(io.StringIO()):
            processed = asyncio.run(run_note_import_pipeline(sources, 0))

        self.assertEqual(sources, processed)
        self.assertIsNot(sources, processed)


if __name__ == "__main__":
    unittest.main()
