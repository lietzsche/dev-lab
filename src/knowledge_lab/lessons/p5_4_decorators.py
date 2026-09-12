"""P5-4: decorator의 함수 wrapping과 호출 경계를 관찰한다."""

from functools import wraps
from time import perf_counter


def log_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs) -> str:
        print("before call")
        result = function(*args, **kwargs)
        print("after call")
        return result

    return wrapper


@log_call
def make_note_label(title: str) -> str:
    """Create a display label for a note."""
    print("original called")
    return f"Note: {title}"


@log_call
def make_note_summary(
    title: str,
    content: str,
    prefix: str = "NOTE",
) -> str:
    return f"[{prefix}] {title}: {content}"


def measure_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = function(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"elapsed seconds: {elapsed:.6f}")
        return result

    return wrapper


@measure_time
def count_characters(text: str) -> int:
    return len(text)


def trace_category(category: str):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(f"wrapper called: {category}")
            return function(*args, **kwargs)

        return wrapper

    return decorator


@trace_category("learning")
def format_title(title: str) -> str:
    return title.upper()


routes = {}


def route(path: str):
    def decorator(function):
        routes[path] = function
        return function

    return decorator


@route("/notes")
def list_notes() -> list[str]:
    return ["Python", "Generator"]


def run() -> None:
    """Run the current decorator exercise."""
    print()
    print("P5-4 decorator 시작")

    print(f"registered routes: {routes.keys()}")
    print(f"routes['/notes'] is list_notes: {routes['/notes'] is list_notes}")
    print(f"route result: {routes['/notes']()}")
