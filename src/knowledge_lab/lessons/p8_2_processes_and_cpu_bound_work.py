"""P8-2: process와 CPU-bound 작업의 실행 경계를 관찰한다."""

import multiprocessing
import os
import pickle
import threading
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def calculate_note_checksum(iterations: int) -> int:
    current_process_id = os.getpid()
    current_thread_name = threading.current_thread().name
    print(f"process id: {current_process_id}")
    print(f"thread name: {current_thread_name}")

    checksum = 0
    for number in range(iterations):
        checksum += number * number
        checksum = checksum % 1_000_003

    return checksum


def append_process_marker(values: list[str]) -> None:
    print(f"child pid: {os.getpid()}")
    print(f"in child, before values: {values}")
    values.append("child")
    print(f"in child, after values: {values}")


def serialize_note_titles(titles: list[str]) -> bytes:
    return pickle.dumps(titles)


def deserialize_note_titles(payload: bytes) -> list[str]:
    titles: object = pickle.loads(payload)
    if not isinstance(titles, list):
        raise ValueError("invalid note titles")

    for title in titles:
        if not isinstance(title, str):
            raise ValueError("invalid note titles")

    return titles


def measure_pickle_round_trip(titles: list[str]) -> tuple[int, float]:
    start_time = time.perf_counter()
    payload = serialize_note_titles(titles)
    _ = deserialize_note_titles(payload)
    duration = time.perf_counter() - start_time
    return (len(payload), duration)


def calculate_checksums_with_threads(
    workloads: list[int],
    max_workers: int,
) -> list[int]:
    with ThreadPoolExecutor(
        max_workers=max_workers, thread_name_prefix="checksum"
    ) as executor:
        return list(executor.map(calculate_note_checksum, workloads))


def calculate_checksums_with_processes(
    workloads: list[int],
    max_workers: int,
) -> list[int]:
    context = multiprocessing.get_context("spawn")
    with ProcessPoolExecutor(max_workers=max_workers, mp_context=context) as executor:
        return list(executor.map(calculate_note_checksum, workloads))


def run() -> None:
    """Run the current process and CPU-bound work exercise."""
    print()
    print("P8-2 process와 CPU-bound work 시작")

    workloads = [2_000_000, 2_000_000]
    sequential_start_time = time.perf_counter()
    sequential_results = [calculate_note_checksum(workload) for workload in workloads]
    print(f"sequential duration: {time.perf_counter() - sequential_start_time}")
    print(f"sequential results: {sequential_results}")
    threaded_start_time = time.perf_counter()
    threaded_results = calculate_checksums_with_threads(workloads, 2)
    print(f"threaded duration: {time.perf_counter() - threaded_start_time}")
    print(f"threaded results: {threaded_results}")
    print(f"results equal: {sequential_results == threaded_results}")

    processes_start_time = time.perf_counter()
    processes_results = calculate_checksums_with_processes(workloads, 2)
    print(f"processes duration: {time.perf_counter() - processes_start_time}")
    print(f"processes results: {processes_results}")
    print(
        f"results equal: {processes_results == sequential_results and processes_results == threaded_results}"
    )
