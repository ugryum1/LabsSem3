import unittest
from rk1 import (
    books, libraries, booksLibraries,
    query_one_to_many,
    query_books_count_by_library,
    query_many_to_many_author_ov
)


class TestRK1(unittest.TestCase):
    def test_query_one_to_many(self):
        result = query_one_to_many(books, libraries)
        self.assertTrue(len(result) > 0)
        self.assertEqual(result[0][0], "Война и мир")


    def test_query_books_count_by_library(self):
        result = query_books_count_by_library(books, libraries)
        self.assertIn(("Центральная городская библиотека", 2), result)


    def test_query_many_to_many_author_ov(self):
        result = query_many_to_many_author_ov(books, libraries, booksLibraries)
        authors = [item[1] for item in result]

        self.assertIn("Булгаков", authors)
        self.assertIn("Лермонтов", authors)
        self.assertNotIn("Достоевский", authors)


if __name__ == "__main__":
    unittest.main()
