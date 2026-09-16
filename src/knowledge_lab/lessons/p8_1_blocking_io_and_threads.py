"""P8-1: blocking I/O와 thread의 실행 경계를 관찰한다."""

import threading
import time


def load_note_source(source: str, delay_seconds: float) -> str:
    print(f"current thread name: {threading.current_thread().name}")
    print(f"load start: {source}")
    time.sleep(delay_seconds)
    print(f"load end: {source}")
    return source


def load_sources_sequentially(
    sources: list[str],
    delay_seconds: float,
) -> list[str]:
    results: list[str] = []
    for source in sources:
        result = load_note_source(source, delay_seconds)
        results.append(result)

    return results


def load_sources_with_threads(
    sources: list[str],
    delay_seconds: float,
) -> list[str]:
    results: list[str] = []
    loaders: list[threading.Thread] = []
    name_index = 1
    for source in sources:
        loader = threading.Thread(
            target=load_note_source_into,
            args=(source, delay_seconds, results),
            name=f"loader-{name_index}",
        )
        loaders.append(loader)
        loader.start()
        name_index += 1

    for loader in loaders:
        loader.join()

    return results


def load_note_source_into(
    source: str,
    delay_seconds: float,
    results: list[str],
) -> None:
    result = load_note_source(source, delay_seconds)
    results.append(result)


def increment_count_without_lock(
    state: dict[str, int],
    increments: int,
) -> None:
    for _ in range(0, increments):
        current_count = state["count"]
        time.sleep(0)
        state["count"] = current_count + 1


def increment_count_with_lock(
    state: dict[str, int], increments: int, lock: threading.Lock
) -> None:
    for _ in range(0, increments):
        with lock:
            current_count = state["count"]
            time.sleep(0)
            state["count"] = current_count + 1


def run() -> None:
    """Run the current blocking I/O and thread exercise."""
    print()
    print("P8-1 blocking I/O와 thread 시작")

    start_time = time.perf_counter()
    increments = 1000
    state = {"count": 0}
    lock = threading.Lock()
    workers: list[threading.Thread] = []
    for idx in range(0, 4):
        worker = threading.Thread(
            target=increment_count_with_lock,
            args=(state, increments, lock),
            name=f"worker-{idx}",
        )
        worker.start()
        workers.append(worker)
    for w in workers:
        w.join()
    expected_count = increments * len(workers)
    elapsed_seconds = time.perf_counter() - start_time
    print(f"duration: {elapsed_seconds}")
    print(f"expected count: {expected_count}")
    print(f"actual count: {state['count']}")
    print(f"lost count: {expected_count - state['count']}")
