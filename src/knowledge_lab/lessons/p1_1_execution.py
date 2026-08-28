"""P1-1: module execution and the first note output."""


def run() -> None:
    """Display the first note and inspect its runtime values."""
    title = "실제 제목"
    content = "실제 내용"

    print(f"P1-1 module __name__: {__name__!r}")
    print(f"제목 repr: {repr(title)}")
    print(f"제목 type: {type(title)}")
    print(f"내용 type: {type(content)}")
    print(f"제목: {title}")
    print(f"내용: {content}")
