import asyncio
from fastapi.testclient import TestClient
from fastmcp import Client
from fastmcp.client.client import CallToolResult

from knowledge_lab.lessons.p11_1_tool_contract import search_notes
from knowledge_lab.lessons.p11_2_fastmcp_server import mcp
from knowledge_lab.lessons.p11_4_mcp_testing_and_client import app


async def call_search_notes_with_client() -> CallToolResult:
    async with Client(mcp) as client:
        return await client.call_tool("search_notes", {"query": "python", "limit": 1})


def test_search_notes_direct_call_is_deterministic() -> None:
    first = search_notes("python", limit=1)
    second = search_notes("python", limit=1)
    assert first == {"query": "python", "limit": 1, "titles": ["Python iterator"]}
    assert first == second
    assert first is not second


def test_search_notes_through_mcp_client() -> None:
    result = asyncio.run(call_search_notes_with_client())
    assert type(result) is CallToolResult
    assert result.structured_content == {
        "query": "python",
        "limit": 1,
        "titles": ["Python iterator"],
    }


def test_fastapi_and_mcp_share_search_contract() -> None:
    with TestClient(app) as client:
        http_response = client.get("/notes/search?query=python&limit=1")
        mcp_result = asyncio.run(call_search_notes_with_client())
        assert http_response.status_code == 200
        assert http_response.json() == mcp_result.structured_content
