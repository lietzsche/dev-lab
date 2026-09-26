"""Public behavior tests for the P11-1 tool contract lesson."""

import json
import unittest

from knowledge_lab.lessons.p11_1_tool_contract import search_notes


class ToolContractTest(unittest.TestCase):
    def test_search_notes_normalizes_query_and_limits_matches(self) -> None:
        result = search_notes(" PYTHON ", limit=1)

        self.assertEqual(
            {
                "query": " PYTHON ",
                "limit": 1,
                "titles": ["Python iterator"],
            },
            result,
        )

    def test_search_notes_rejects_blank_query(self) -> None:
        with self.assertRaisesRegex(ValueError, "query must not be blank"):
            search_notes("   ")

    def test_search_notes_rejects_non_positive_limit(self) -> None:
        with self.assertRaisesRegex(ValueError, "limit must be at least 1"):
            search_notes("python", limit=0)

    def test_search_notes_result_is_json_serializable(self) -> None:
        result = search_notes("python", limit=2)

        self.assertEqual(result, json.loads(json.dumps(result)))


if __name__ == "__main__":
    unittest.main()
