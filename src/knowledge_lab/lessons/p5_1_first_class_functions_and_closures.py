"""P5-1: first-class function과 closure를 관찰한다."""


def format_note_title(title: str) -> str:
    return f"[NOTE] {title}"


def apply_title_formatter(formatter, title: str) -> str:
    return formatter(title)


def get_title_formatter():
    return format_note_title


def make_note_formatter(prefix: str):
    def format_with_prefix(title: str) -> str:
        return f"{prefix} {title}"

    return format_with_prefix


def make_prefix_reader(prefix: str):
    def read_prefix() -> str:
        return prefix

    return read_prefix


def make_prefix_readers(prefixes: list[str]):
    readers = []
    for prefix in prefixes:
        readers.append(make_prefix_reader(prefix))
    return readers


def make_note_counter():
    count = 0

    def count_note() -> int:
        nonlocal count
        count += 1
        return count

    return count_note


def run() -> None:
    """Run the current first-class function and closure exercise."""
    print()
    print("P5-1 first-class function과 closure 시작")

    formatter = format_note_title
    print(f"formatter is format_note_title: {formatter is format_note_title}")
    print(f"formatted by alias: {formatter('Python function')}")

    formatted_title = apply_title_formatter(
        format_note_title,
        "First-class function",
    )
    print(f"formatted by argument: {formatted_title}")

    returned_formatter = get_title_formatter()
    print(
        "returned formatter is format_note_title: "
        f"{returned_formatter is format_note_title}"
    )
    print(f"formatted by returned function: {returned_formatter('Returned function')}")

    prefix = "[NOTE]"
    note_formatter = make_note_formatter(prefix)
    prefix_cell = note_formatter.__closure__[0]

    print(f"closure result: {note_formatter('Closure')}")
    print(f"closure cell value: {prefix_cell.cell_contents!r}")
    print(f"closure value is prefix: {prefix_cell.cell_contents is prefix}")

    todo_formatter = make_note_formatter("[TODO]")
    todo_prefix_cell = todo_formatter.__closure__[0]
    print(f"todo closure result: {todo_formatter('Independent cell')}")
    print(f"formatters are same object: {note_formatter is todo_formatter}")
    print(f"closure cells are same object: {prefix_cell is todo_prefix_cell}")

    prefix_readers = make_prefix_readers(["[NOTE]", "[TODO]", "[DONE]"])
    values = [reader() for reader in prefix_readers]
    print(f"reader values: {values!r}")
    first_reader_cell = prefix_readers[0].__closure__[0]
    last_reader_cell = prefix_readers[-1].__closure__[0]
    print(f"reader cells are same object: {first_reader_cell is last_reader_cell}")

    counter = make_note_counter()
    print(f"first note count: {counter()}")
    print(f"second note count: {counter()}")
