"""Public behavior tests for the P11-2 FastMCP server lesson."""

import asyncio
import unittest

from knowledge_lab.lessons.p11_2_fastmcp_server import (
    create_note,
    created_titles,
    get_note,
    mcp,
)


class FastMCPServerTest(unittest.TestCase):
    def setUp(self) -> None:
        created_titles.clear()

    def test_server_exposes_note_tools_with_descriptions(self) -> None:
        tools = asyncio.run(mcp.list_tools())
        tools_by_name = {tool.name: tool for tool in tools}

        self.assertEqual(
            {"search_notes", "get_note", "create_note"}, set(tools_by_name)
        )
        self.assertEqual("Knowledge Lab", mcp.name)
        self.assertEqual(
            "Get a note title by its numeric identifier.",
            tools_by_name["get_note"].description,
        )
        self.assertEqual(
            ["query"], tools_by_name["search_notes"].parameters["required"]
        )

    def test_create_note_normalizes_title_and_updates_owned_state(self) -> None:
        result = create_note("  FastMCP server  ")

        self.assertEqual("FastMCP server", result)
        self.assertEqual(["FastMCP server"], created_titles)

    def test_create_note_rejects_blank_title(self) -> None:
        with self.assertRaisesRegex(ValueError, "title must not be blank"):
            create_note("   ")

        self.assertEqual([], created_titles)

    def test_get_note_reports_missing_identifier(self) -> None:
        self.assertEqual("Python iterator", get_note(1))

        with self.assertRaisesRegex(ValueError, "note not found: 2"):
            get_note(2)

    def test_registered_search_tool_returns_structured_content(self) -> None:
        tools = asyncio.run(mcp.list_tools())
        search_tool = next(tool for tool in tools if tool.name == "search_notes")

        result = asyncio.run(search_tool.run(arguments={"query": "python"}))

        self.assertFalse(result.is_error)
        self.assertEqual(
            {
                "query": "python",
                "limit": 5,
                "titles": ["Python iterator", "Python MCP"],
            },
            result.structured_content,
        )


if __name__ == "__main__":
    unittest.main()
