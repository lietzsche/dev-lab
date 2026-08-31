"""P4-1: exceptions and tracebacks."""


class NoteNotFoundError(LookupError):
    pass


class InvalidNoteIdError(ValueError):
    pass


class EmptyTitleError(ValueError):
    pass


def find_note(note_id: int, notes: dict[int, str]) -> str:
    try:
        return notes[note_id]
    except KeyError as error:
        raise NoteNotFoundError(f"note not found: {note_id}") from error


def parse_note_id(raw_id: str) -> int:
    try:
        return int(raw_id)
    except ValueError as error:
        raise InvalidNoteIdError(f"invalid note id: {raw_id!r}") from error


def require_title(title: str) -> str:
    if not title.strip():
        raise EmptyTitleError("title must not be empty")
    return title


def create_label(title: str) -> str:
    return f"NOTE: {require_title(title)}"


def show_label(title: str) -> None:
    try:
        label = create_label(title)
    except ValueError as error:
        print(f"error type: {type(error)}")
        print(f"error repr: {repr(error)}")
    else:
        print(f"label: {label}")
    finally:
        print(f"finished: {title!r}")


def run() -> None:
    """Run exception and traceback experiments added during P4-1."""
    print()
    print("Run exception and traceback experiments added during P4-1.")
    show_label("Python")
    show_label("")
    try:
        parse_note_id("unknown")
    except InvalidNoteIdError as error:
        print(f"converted error: {error!r}")
        print(f"cause type: {type(error.__cause__)}")
        print(f"cause repr: {error.__cause__!r}")
    try:
        find_note(2, {1: "Python"})
    except NoteNotFoundError as error:
        print(f"domain error: {error!r}")
        print(f"infrastructure cause: {error.__cause__!r}")
