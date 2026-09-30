"""P11-4: MCP test와 client 경계를 관찰한다."""

from fastapi import FastAPI

from knowledge_lab.lessons.p11_1_tool_contract import SearchNotesResult, search_notes


app = FastAPI()


@app.get("/notes/search")
def search_notes_http(query: str, limit: int = 5) -> SearchNotesResult:
    return search_notes(query, limit)


def run() -> None:
    """Run the current MCP testing and client exercise."""
    print()
    print("P11-4 MCP test와 client 시작")
