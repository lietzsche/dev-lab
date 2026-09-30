"""P11-2: FastMCP server 경계를 관찰한다."""

import asyncio

from fastmcp import FastMCP

from knowledge_lab.lessons.p11_1_tool_contract import search_notes


mcp = FastMCP("Knowledge Lab")
mcp.tool(search_notes, description="제목에서 검색어와 일치하는 노트를 찾는다.")


created_titles: list[str] = []


def get_note(note_id: int) -> str:
    """Get a note title by its numeric identifier."""
    if note_id == 1:
        return "Python iterator"
    raise ValueError(f"note not found: {note_id}")


mcp.tool(get_note)


def create_note(title: str) -> str:
    """Create a note with a normalized title."""
    add_title = title.strip()
    if add_title == "":
        raise ValueError("title must not be blank")
    created_titles.append(add_title)
    return add_title


mcp.tool(create_note)


def run() -> None:
    """Run the current FastMCP server exercise."""
    print()
    print("P11-2 FastMCP server 시작")

    print(f"mcp type: {type(mcp)}")
    print(f"mcp name: {mcp.name}")

    tools = asyncio.run(mcp.list_tools())
    print(f"mcp tools: {tools}")
    print(f"mcp tools type: {type(tools)}")
    print(f"mcp tools length: {len(tools)}")

    return_note = create_note(" FastMCP server ")
    print(f"return note: {return_note}")
    print(f"created titles: {created_titles}")
    for tool in tools:
        print(f"tool name: {tool.name}")
        print(f"tool description: {tool.description}")
