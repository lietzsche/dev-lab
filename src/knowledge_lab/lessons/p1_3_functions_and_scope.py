"""P1-3: functions and scope."""


def remember_title(title, history=None):
    if history is None:
        history = []
    history.append(title)
    return history


def show_enclosing_scope():
    message = "enclosing scope"

    def show_message():
        print(f"message: {message}")

    show_message()

    def change_message():
        nonlocal message
        message = "changed enclosing scope"

    change_message()
    print(f"message after change: {message}")


def increase_note_count(note_count):
    return note_count + 1


def make_note_label(title, prefix="NOTE"):
    return f"[{prefix}] {title}"


def run() -> None:
    print()
    print("""Run function and scope experiments added during P1-3.""")
    label = make_note_label(title="Python 함수")
    print(label)
    label = make_note_label(title="Python 함수", prefix="TODO")
    print(label)
    note_count = 1
    print(f"before: {note_count}")
    note_count = increase_note_count(note_count)
    print(f"after: {note_count}")

    show_enclosing_scope()

    print(len("Knowledge Lab"))
    print(len.__module__)

    history = remember_title("First")
    print(f"history: {history}")
    history = remember_title("Second")
    print(f"history: {history}")
