"""P6-3: test의 구조와 boundary, test double의 역할을 구분한다."""


def normalize_title(title: str) -> str:
    """Return a title without outer whitespace."""
    return title.strip()


def run() -> None:
    """Run the current test design exercise."""
    print()
    print("P6-3 test 설계 시작")
