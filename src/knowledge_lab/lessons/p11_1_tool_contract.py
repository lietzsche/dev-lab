"""P11-1: tool contract 경계를 관찰한다."""

from inspect import signature
import json
from typing import TypedDict, get_type_hints


class SearchNotesResult(TypedDict):
    query: str
    limit: int
    titles: list[str]


def search_notes(query: str, limit: int = 5) -> SearchNotesResult:
    titles = ["Python iterator", "FastAPI dependency", "Python MCP"]
    normalized_query = query.strip().casefold()
    if not normalized_query:
        raise ValueError("query must not be blank")
    if limit < 1:
        raise ValueError("limit must be at least 1")
    matching_titles: list[str] = []
    for title in titles:
        if normalized_query in title.casefold():
            matching_titles.append(title)
    return {"query": query, "limit": limit, "titles": matching_titles[:limit]}


def run() -> None:
    """Run the current tool contract exercise."""
    print()
    print("P11-1 tool contract 시작")

    result = search_notes(" python ", limit=2)
    print(f"tool result type: {type(result)}")
    print(f"tool result: {result}")

    try:
        search_notes("   ")
    except ValueError as error:
        print(f"blank query error: {error!r}")
    try:
        search_notes("python", limit=0)
    except ValueError as error:
        print(f"invalid limit error: {error!r}")

    print(f"tool signature: {signature(search_notes)}")
    print(f"tool type hints: {get_type_hints(search_notes)}")
    print(f"result fields: {get_type_hints(SearchNotesResult)}")

    serialized_result = json.dumps(result, ensure_ascii=False)
    restored_result = json.loads(serialized_result)
    print(f"serialized result: {serialized_result}")
    print(f"restored result type: {type(restored_result)}")
    print(f"round trip preserved: {restored_result == result}")
