"""P1-4: control flow and pattern matching."""


def show_content_truthy(content):
    if content:
        print("content: present")
    else:
        print("content: empty")


def content_state(content):
    return "present" if content else "empty"


def find_character(text, target):
    for char in text:
        if char == target:
            print(f"found: {char}")
            break
    else:
        print(f"not found: {target}")


def describe_command(command):
    match command:
        case "create" | "add":
            return "create note"
        case "search":
            return "search notes"
        case _:
            return "unknown command"


def run() -> None:
    """Run control-flow experiments added during P1-4."""
    print()
    print("Run control-flow experiments added during P1-4.")
    content = ""
    print(f"content truthy: {bool(content)}")
    content = "Python truthiness"
    print(f"content truthy: {bool(content)}")
    show_content_truthy("")
    show_content_truthy("Python if")
    print(f"content state: {content_state('')}")
    print(f"content state: {content_state('Python')}")

    for character in "Lab":
        print(f"character: {character}")
    print(f"last character: {character}")

    note_numbers = range(1, 4)
    print(f"note numbers repr: {repr(note_numbers)}")
    print(f"note numbers type: {type(note_numbers)}")
    for note_number in note_numbers:
        print(f"note number: {note_number}")

    for position, character in enumerate("Lab", start=1):
        print(f"position: {position}, character: {character}")

    for note_number, character in zip(range(1, 4), "Lab", strict=True):
        print(f"note {note_number}: {character}")

    remaining = 3
    while remaining > 0:
        print(f"remaining: {remaining}")
        remaining = remaining - 1
    print(f"remaining after loop: {remaining}")

    for char in "Knowledge":
        if char == "l":
            print(f"found: {char}")
            break
        print(f"checking: {char}")
    print("search finished")

    for char in "Lab":
        if char == "a":
            continue
        print(f"kept: {char}")
    print("filter finished")

    find_character("Lab", "a")
    find_character("Lab", "z")

    print(f"command: {describe_command('create')}")
    print(f"command: {describe_command('add')}")
    print(f"command: {describe_command('delete')}")
