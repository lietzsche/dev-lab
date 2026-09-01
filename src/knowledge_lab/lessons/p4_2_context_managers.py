"""P4-2: context manager와 resource lifetime을 관찰한다."""

from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field
from io import StringIO


@contextmanager
def managed_text_stream(text: str) -> Iterator[StringIO]:
    stream = StringIO(text)
    try:
        yield stream
    finally:
        stream.close()


@dataclass
class ManagedStream:
    text: str
    stream: StringIO = field(init=False)
    suppress_error: bool = False

    def __post_init__(self) -> None:
        self.stream = StringIO(self.text)

    def __enter__(self) -> StringIO:
        return self.stream

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        self.stream.close()
        print(f"exit exc_type: {exc_type}")
        print(f"exit exc_value: {exc_value!r}")
        print(f"exit traceback is None: {traceback is None}")
        return self.suppress_error


def run() -> None:
    """Run the current context manager exercise."""
    first_stream = StringIO("first hello")
    print(f"before block stream closed: {first_stream.closed}")
    with first_stream as open_stream:
        print(f"open stream is stream: {open_stream is first_stream}")
        print(f"open stream read: {open_stream.read()}")
        print(f"in block, open stream closed: {open_stream.closed}")
    print(f"after block stream closed: {first_stream.closed}")

    second_stream = StringIO("second hello")
    try:
        with second_stream as open_stream:
            print(f"open stream closed: {open_stream.closed}")
            raise RuntimeError("중간 작업 실패")
    except RuntimeError as error:
        print(f"error: {error!r}")

    print(f"after exception block stream closed: {second_stream.closed}")

    third_stream = StringIO("third hello")
    try:
        raise RuntimeError("수동 처리 중 실패")
        third_stream.close()
    except RuntimeError as error:
        print(f"error: {error!r}")

    print(f"after exception block stream closed: {third_stream.closed}")
    third_stream.close()

    first_class_stream = ManagedStream("class hello")
    with first_class_stream as stream:
        print(f"class stream is stream: {first_class_stream.stream is stream}")
        print(f"stream read: {stream.read()}")
    print(f"class_stream's stream closed: {first_class_stream.stream.closed}")

    second_class_stream = ManagedStream("error class hello")
    try:
        with second_class_stream as stream:
            raise RuntimeError("error is not bad")
    except RuntimeError as error:
        print(f"except error type: {type(error)}")
        print(f"except error value: {error!r}")
    print(f"second class stream's stream closed: {second_class_stream.stream.closed}")

    third_class_stream = ManagedStream("suppressed", suppress_error=True)
    with third_class_stream as stream:
        raise RuntimeError("error is not bad")
    print("continued after with")
    print(f"third class stream's stream closed: {third_class_stream.stream.closed}")

    with managed_text_stream("generator hello") as stream:
        print(f"stream read: {stream.read()}")
        print(f"in block stream closed: {stream.closed}")
    print(f"after block stream closed: {stream.closed}")

    try:
        with managed_text_stream("generator error") as error_stream:
            print(f"in block stream closed: {error_stream.closed}")
            raise RuntimeError("generator 작업 실패")
    except RuntimeError as error:
        print(f"error: {error!r}")

    print(f"after exception stream closed: {error_stream.closed}")
    
