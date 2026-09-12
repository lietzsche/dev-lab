"""P1-2: names, objects, and runtime types."""


def run() -> None:
    """Observe one name being bound to objects of different types."""
    status = "원하는 문자열"
    print(f"status: {status}, status type: {type(status)}")

    status = 3
    print(f"status: {status}, status type: {type(status)}")

    source = None
    print(f"source: {source}, source type: {type(source)}")
    print(f"source is None: {source is None}")

    published = False
    print(f"published: {published}, published type: {type(published)}")
    published = True
    print(f"published: {published}, published type: {type(published)}")

    relevance = 1.0
    print(f"relevance: {relevance}, relevance type: {type(relevance)}")

    same_relevance = relevance
    print(f"same_relevance id: {id(same_relevance)}, relevance id: {id(relevance)}")
    print(f"same_relevance is relevance: {same_relevance is relevance}")

    expected_relevance = float("1.0")
    actual_relevance = float("1.0")
    print(
        f"expected_relevance id: {id(expected_relevance)}, "
        f"actual_relevance id: {id(actual_relevance)}"
    )
    print(
        "expected_relevance == actual_relevance: "
        f"{expected_relevance == actual_relevance}"
    )
    print(
        "expected_relevance is actual_relevance: "
        f"{expected_relevance is actual_relevance}"
    )
