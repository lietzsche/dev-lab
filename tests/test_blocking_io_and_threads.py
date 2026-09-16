"""Public behavior tests for P8-1 blocking I/O and threads."""

import io
import threading
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from knowledge_lab.lessons.p8_1_blocking_io_and_threads import (
    increment_count_with_lock,
    load_note_source,
    load_sources_sequentially,
    load_sources_with_threads,
)


class BlockingIoAndThreadsTest(unittest.TestCase):
    def test_load_note_source_blocks_in_calling_thread_and_returns_source(self) -> None:
        output = io.StringIO()

        with patch(
            "knowledge_lab.lessons.p8_1_blocking_io_and_threads.time.sleep"
        ) as sleep:
            with redirect_stdout(output):
                result = load_note_source("Python docs", 0.2)

        sleep.assert_called_once_with(0.2)
        self.assertEqual("Python docs", result)
        self.assertIn("current thread name: MainThread", output.getvalue())

    def test_sequential_loader_preserves_input_order(self) -> None:
        sources = ["Python docs", "SQLite docs"]

        with patch(
            "knowledge_lab.lessons.p8_1_blocking_io_and_threads.load_note_source",
            side_effect=lambda source, _: source,
        ):
            results = load_sources_sequentially(sources, 0.2)

        self.assertEqual(sources, results)
        self.assertIsNot(sources, results)

    def test_threaded_loader_collects_every_result_after_join(self) -> None:
        sources = ["Python docs", "SQLite docs"]

        with redirect_stdout(io.StringIO()):
            results = load_sources_with_threads(sources, 0)

        self.assertCountEqual(sources, results)
        self.assertIsNot(sources, results)

    def test_shared_lock_prevents_lost_updates(self) -> None:
        state = {"count": 0}
        lock = threading.Lock()
        workers = [
            threading.Thread(
                target=increment_count_with_lock,
                args=(state, 100, lock),
            )
            for _ in range(4)
        ]

        for worker in workers:
            worker.start()
        for worker in workers:
            worker.join()

        self.assertEqual(400, state["count"])


if __name__ == "__main__":
    unittest.main()
