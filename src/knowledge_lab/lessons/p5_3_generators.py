"""P5-3: generator의 lazy execution과 상태 보존을 관찰한다."""

from knowledge_lab.lessons.p3_3_dataclasses_and_value_objects import Note


def generate_note_titles(titles: list[str]):
    print("generator body started")
    for title in titles:
        print(f"before yield: {title}")
        yield title
        print(f"resumed after: {title}")


def uppercase_titles(titles):
    for title in titles:
        print(f"transforming: {title}")
        yield title.upper()


def chain_note_groups(
    first_titles: list[str],
    second_titles: list[str],
):
    print(f"first group: {first_titles}")
    yield from generate_note_titles(first_titles)
    print(f"second group: {second_titles}")
    yield from generate_note_titles(second_titles)


def stream_note_titles(notes: list[Note], keyword: str):
    keyword_lower = keyword.lower()
    for note in notes:
        print(f"checking note: {note.title}")
        if keyword_lower in note.title.lower():
            yield note.title


def run() -> None:
    """Run the current generator exercise."""
    print()
    print("P5-3 generator 시작")

    contents = [
        Note(title="Rust ownership", content="Rust content"),
        Note(title="Python generator", content="Python first content"),
        Note(title="Python asyncio", content="Python second content"),
    ]
    stream = stream_note_titles(contents, "PYTHON")
    print("search stream created")
    print(f"first match: {next(stream)}")
