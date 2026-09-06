"""P5-2: iterable과 iterator protocol을 관찰한다."""


class NoteTitleIterator:
    def __init__(self, titles: list[str]) -> None:
        self._titles = titles
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self._index >= len(self._titles):
            raise StopIteration
        local_name = self._titles[self._index]
        self._index += 1
        return local_name


class NoteTitles:
    def __init__(self, titles: list[str]) -> None:
        self._titles = titles.copy()

    def __iter__(self):
        return NoteTitleIterator(self._titles)


def run() -> None:
    """Run the current iterable and iterator exercise."""
    print()
    print("P5-2 iterable과 iterator 시작")

    note_titles = ["Python", "FastAPI"]
    first_iterator = iter(note_titles)
    second_iterator = iter(note_titles)
    print(f"first iterator type: {type(first_iterator)}")
    print(
        f"first iterator is note titles: {first_iterator is note_titles}"
    )
    print(
        "first iterator is second iterator: "
        f"{first_iterator is second_iterator}"
    )
    print(
        "iter(first iterator) is first iterator: "
        f"{iter(first_iterator) is first_iterator}"
    )

    print(f"first iterator next: {next(first_iterator)}")
    print(f"first iterator next: {next(first_iterator)}")
    print(f"second iterator next: {next(second_iterator)}")
    print(f"note titles: {note_titles}")

    try:
        print(next(first_iterator))
    except StopIteration as error:
        print(f"exhausted error type: {type(error)}")
        print(f"exhausted error repr: {error!r}")
    print(f"first iterator after exhaustion: {next(first_iterator, 'END')}")
    print(f"second iterator remaining value: {next(second_iterator)}")

    third_iterator = iter(note_titles)
    for title in third_iterator:
        print(f"for title: {title}")
    print(f"third iterator after for: {next(third_iterator, 'END')}")

    shared_iterator = iter(note_titles)
    first_pass = list(shared_iterator)
    second_pass = list(shared_iterator)
    iterable_first_pass = list(note_titles)
    iterable_second_pass = list(note_titles)
    print(f"iterator first pass: {first_pass}")
    print(f"iterator second pass: {second_pass}")
    print(f"iterable first pass: {iterable_first_pass}")
    print(f"iterable second pass: {iterable_second_pass}")
    print(
        "iterable passes are same object: "
        f"{iterable_first_pass is iterable_second_pass}"
    )

    note_titles_collection = NoteTitles(note_titles)
    first_custom_iterator = iter(note_titles_collection)
    second_custom_iterator = iter(note_titles_collection)
    custom_iterable_first_pass = list(note_titles_collection)
    custom_iterable_second_pass = list(note_titles_collection)
    print(
        "custom iterators are same object: "
        f"{first_custom_iterator is second_custom_iterator}"
    )
    print(f"custom iterator type: {type(first_custom_iterator)}")
    print(f"custom iterable first pass: {custom_iterable_first_pass}")
    print(f"custom iterable second pass: {custom_iterable_second_pass}")

    print(
        "iter(custom iterator) is itself: "
        f"{iter(first_custom_iterator) is first_custom_iterator}"
    )
