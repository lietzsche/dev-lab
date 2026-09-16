"""P8-3: coroutine과 event loop의 실행 경계를 관찰한다."""

import asyncio
import threading
import time


async def make_note_title(title: str) -> str:
    print("coroutine body started")
    return title


async def build_note_label(title: str) -> str:
    print("before await")
    title = await make_note_title(title)
    print("after await")
    return f"Note: {title}"


async def run_note_task() -> str:
    print("before create task")
    task = asyncio.create_task(
        build_note_label("Python docs"),
        name="note-label",
    )
    print(f"task name: {task.get_name()}, task done: {task.done()}")
    result = await task
    print(f"task name: {task.get_name()}, task done: {task.done()}")
    return result


async def load_note_source(
    source: str,
    delay_seconds: float,
) -> str:
    print(f"load start: {source}")
    await asyncio.sleep(delay_seconds)
    print(f"load end: {source}")
    return source


async def load_sources_sequentially(
    sources: list[str],
    delay_seconds: float,
) -> list[str]:
    results: list[str] = []
    for source in sources:
        result = await load_note_source(source, delay_seconds)
        results.append(result)
    return results


async def load_sources_concurrently(
    sources: list[str],
    delay_seconds: float,
) -> list[str]:
    tasks: list[asyncio.Task[str]] = []
    for source in sources:
        task = asyncio.create_task(load_note_source(source, delay_seconds))
        tasks.append(task)

    results: list[str] = []
    for task in tasks:
        result = await task
        results.append(result)

    return results


def load_note_source_blocking(
    source: str,
    delay_seconds: float,
) -> str:
    print(f"thread name: {threading.current_thread().name}")
    print(f"blocking start: {source}")
    time.sleep(delay_seconds)
    print(f"blocking end: {source}")
    return source


async def load_sources_with_to_thread(
    sources: list[str],
    delay_seconds: float,
) -> list[str]:
    tasks: list[asyncio.Task[str]] = [
        asyncio.create_task(
            asyncio.to_thread(load_note_source_blocking, source, delay_seconds)
        )
        for source in sources
    ]
    return [await task for task in tasks]


def run() -> None:
    """Run the current coroutine and event loop exercise."""
    print()
    print("P8-3 coroutine과 event loop 시작")

    start_time = time.perf_counter()
    result = asyncio.run(
        load_sources_with_to_thread(["Python docs", "SQLite docs"], 0.2)
    )
    duration = time.perf_counter() - start_time
    print(f"after asyncio.run: {result}")
    print(f"duration: {duration}")
