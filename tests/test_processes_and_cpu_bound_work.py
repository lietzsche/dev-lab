"""Public behavior tests for P8-2 processes and CPU-bound work."""

import io
import multiprocessing
import pickle
import unittest
from contextlib import redirect_stdout

from knowledge_lab.lessons.p8_2_processes_and_cpu_bound_work import (
    append_process_marker,
    calculate_checksums_with_processes,
    calculate_checksums_with_threads,
    calculate_note_checksum,
    deserialize_note_titles,
    measure_pickle_round_trip,
    serialize_note_titles,
)


class ProcessesAndCpuBoundWorkTest(unittest.TestCase):
    def test_checksum_is_deterministic(self) -> None:
        iterations = 1_000
        expected = sum(number * number for number in range(iterations)) % 1_000_003

        with redirect_stdout(io.StringIO()):
            result = calculate_note_checksum(iterations)

        self.assertEqual(expected, result)

    def test_pickle_round_trip_creates_an_equal_fresh_list(self) -> None:
        titles = ["Python", "SQLite"]

        payload = serialize_note_titles(titles)
        restored = deserialize_note_titles(payload)

        self.assertIsInstance(payload, bytes)
        self.assertEqual(titles, restored)
        self.assertIsNot(titles, restored)

    def test_deserializer_rejects_invalid_title_shapes(self) -> None:
        invalid_values = [{"title": "Python"}, ["Python", 42]]

        for invalid_value in invalid_values:
            with self.subTest(value=invalid_value):
                with self.assertRaisesRegex(ValueError, "invalid note titles"):
                    deserialize_note_titles(pickle.dumps(invalid_value))

    def test_larger_pickle_payload_has_a_larger_serialized_size(self) -> None:
        small_size, _ = measure_pickle_round_trip(["Python"])
        large_size, _ = measure_pickle_round_trip(
            [f"Note {index}" for index in range(1_000)]
        )

        self.assertGreater(large_size, small_size)

    def test_thread_and_process_pools_preserve_checksum_results(self) -> None:
        workloads = [1_000, 2_000]
        with redirect_stdout(io.StringIO()):
            expected = [calculate_note_checksum(workload) for workload in workloads]
            threaded = calculate_checksums_with_threads(workloads, 2)
            processed = calculate_checksums_with_processes(workloads, 2)

        self.assertEqual(expected, threaded)
        self.assertEqual(expected, processed)

    def test_spawned_process_does_not_mutate_parent_list(self) -> None:
        values = ["parent"]
        context = multiprocessing.get_context("spawn")
        process = context.Process(target=append_process_marker, args=(values,))

        process.start()
        process.join()

        self.assertEqual(0, process.exitcode)
        self.assertEqual(["parent"], values)


if __name__ == "__main__":
    unittest.main()
