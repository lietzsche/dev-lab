"""P8-4: cancellation, timeout, backpressure의 경계를 관찰한다."""

import asyncio
import time


async def import_note_source(
    source: str,
    delay_seconds: float,
) -> str:
    print(f"import start: {source}")
    await asyncio.sleep(delay_seconds)
    print(f"import end: {source}")
    return source


async def observe_task_group() -> None:
    async with asyncio.TaskGroup() as group:
        python_task = group.create_task(import_note_source("Python docs", 0.2))
        sqlite_task = group.create_task(import_note_source("SQLite docs", 0.2))
        print(f"in block, python task done: {python_task.done()}")
        print(f"in block, sqlite task done: {sqlite_task.done()}")
    print(f"after block, python task done: {python_task.done()}")
    print(f"after block, sqlite task done: {sqlite_task.done()}")
    print(f"python task result: {python_task.result()}")
    print(f"sqlite task result: {sqlite_task.result()}")


async def fail_note_source(
    source: str,
    delay_seconds: float,
) -> str:
    print(f"import start: {source}")
    await asyncio.sleep(delay_seconds)
    raise ValueError(f"failed to import: {source}")


async def observe_task_group_failure() -> None:
    try:
        async with asyncio.TaskGroup() as group:
            slow_task = group.create_task(import_note_source("slow docs", 1.0))
            fail_task = group.create_task(fail_note_source("Broken docs", 0.1))
    except* ValueError as error_group:
        print(f"error group type: {type(error_group)}")
        print(f"error group exceptions length: {len(error_group.exceptions)}")
        print(f"error group first exception repr: {error_group.exceptions[0]!r}")

    print(f"fail task done: {fail_task.done()}")
    print(f"slow task cancelled: {slow_task.cancelled()}")


async def observe_manual_cancellation() -> None:
    try:
        task = asyncio.create_task(import_note_source("Cancelled docs", 10.0))
        await asyncio.sleep(0)
        return_cancel = task.cancel("import no longer needed")
        print(f"return cancel: {return_cancel}")
        await task
    except asyncio.CancelledError as error:
        print(f"error type: {type(error)}")
        print(f"error repr: {error!r}")

    print(f"task done: {task.done()}")
    print(f"task cancelled: {task.cancelled()}")


async def observe_timeout() -> None:
    start_time = time.perf_counter()
    try:
        async with asyncio.timeout(0.1):
            result = await import_note_source("Timeout docs", 1.0)
            print(f"import result: {result}")
    except TimeoutError as error:
        print(f"error type: {type(error)}")
        print(f"error repr: {error!r}")
        print(f"duration: {time.perf_counter() - start_time}")
    print("after timeout")


async def import_note_source_with_cleanup(
    source: str,
    delay_seconds: float,
) -> str:
    print(f"import start: {source}")
    try:
        await asyncio.sleep(delay_seconds)
        print(f"import end: {source}")
        return source
    except asyncio.CancelledError:
        print(f"cancel received: {source}")
        raise
    finally:
        print(f"cleanup: {source}")


async def observe_cancellation_cleanup() -> None:
    try:
        async with asyncio.timeout(0.1):
            await import_note_source_with_cleanup("Cleanup docs", 1.0)
    except TimeoutError:
        print("outer timeout received")


async def observe_bounded_queue() -> None:
    queue: asyncio.Queue[str] = asyncio.Queue(maxsize=1)
    await queue.put("Python docs")
    print(f"queue size: {queue.qsize()}")
    print(f"queue full: {queue.full()}")
    put_task = asyncio.create_task(queue.put("SQLite docs"))
    await asyncio.sleep(0)
    print(f"second put done before get: {put_task.done()}")
    print(f"queue size: {queue.qsize()}")
    first_item = await queue.get()
    print(f"first item: {first_item}")
    await put_task
    print(f"second put done after get: {put_task.done()}")
    print(f"queue size: {queue.qsize()}")
    second_item = await queue.get()
    print(f"second item: {second_item}")


async def observe_queue_completion() -> None:
    queue: asyncio.Queue[str] = asyncio.Queue(maxsize=2)
    await queue.put("Python docs")
    await queue.put("SQLite docs")
    first_item = await queue.get()
    print(f"first item: {first_item}")
    queue.task_done()
    print("first item processing completed")
    join_task = asyncio.create_task(queue.join())
    await asyncio.sleep(0)
    print(f"join task done after first: {join_task.done()}")
    second_item = await queue.get()
    print(f"second item: {second_item}")
    print(f"queue size: {queue.qsize()}")
    await asyncio.sleep(0)
    print(f"join task done: {join_task.done()}")
    queue.task_done()
    print("second item processing completed")
    await join_task
    print(f"join task done: {join_task.done()}")


async def produce_note_sources(
    queue: asyncio.Queue[str | None],
    sources: list[str],
) -> None:
    for source in sources:
        print(f"put waiting: {source}")
        await queue.put(source)
        print(f"put complete: {source}, queue size: {queue.qsize()}")
    await queue.put(None)
    print("producer finished")


async def consume_note_sources(
    queue: asyncio.Queue[str | None],
    delay_seconds: float,
) -> list[str]:
    processed: list[str] = []
    while True:
        item = await queue.get()
        try:
            if item is None:
                print("consumer finished")
                return processed
            print("process start")
            await asyncio.sleep(delay_seconds)
            processed.append(item)
            print("process complete")
        finally:
            queue.task_done()


async def run_note_import_pipeline(
    sources: list[str],
    delay_seconds: float,
) -> list[str]:
    queue: asyncio.Queue[str | None] = asyncio.Queue(maxsize=1)
    async with asyncio.TaskGroup() as group:
        producer = group.create_task(produce_note_sources(queue, sources))
        consumer = group.create_task(consume_note_sources(queue, delay_seconds))
        await producer
        await queue.join()
    return consumer.result()


def run() -> None:
    """Run the current cancellation, timeout, and backpressure exercise."""
    print()
    print("P8-4 cancellation, timeout, backpressure 시작")

    processed_sources = asyncio.run(
        run_note_import_pipeline(["Python docs", "SQLite docs", "AsyncIO docs"], 0.1)
    )
    print(f"processed sources: {processed_sources}")
