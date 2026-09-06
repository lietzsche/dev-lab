"""Public behavior tests for P5-2 iterables and iterators."""

import unittest

from knowledge_lab.lessons.p5_2_iterables_and_iterators import NoteTitles


class IterablesAndIteratorsTest(unittest.TestCase):
    def test_collection_creates_independent_iterators(self) -> None:
        collection = NoteTitles(["Python", "FastAPI"])

        first_iterator = iter(collection)
        second_iterator = iter(collection)

        self.assertIsNot(first_iterator, second_iterator)
        self.assertIs(iter(first_iterator), first_iterator)
        self.assertEqual("Python", next(first_iterator))
        self.assertEqual("Python", next(second_iterator))
        self.assertEqual("FastAPI", next(first_iterator))

    def test_iterator_stays_exhausted_after_stop_iteration(self) -> None:
        iterator = iter(NoteTitles(["Python"]))
        self.assertEqual("Python", next(iterator))

        with self.assertRaises(StopIteration):
            next(iterator)
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_collection_owns_a_copy_of_source_titles(self) -> None:
        source_titles = ["Python"]
        collection = NoteTitles(source_titles)

        source_titles.append("FastAPI")

        self.assertEqual(["Python"], list(collection))
        self.assertEqual(["Python"], list(collection))
