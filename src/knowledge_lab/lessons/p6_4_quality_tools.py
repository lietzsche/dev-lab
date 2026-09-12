"""P6-4: formatter, lint, type checker의 서로 다른 역할을 확인한다."""


def make_label(title: str, prefix: str = "NOTE") -> str:
    return f"[{prefix}] {title}"


def run() -> None:
    """Run the current quality tools exercise."""
    print()
    print("P6-4 품질 도구 시작")

    print(make_label("Python"))
