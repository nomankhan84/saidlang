"""
Unit Tests for SaidLang Standard Runtime Helpers
"""
import unittest
import os
import tempfile
from saidlang.runtime import (
    read_file,
    write_file,
    append_file,
    random_number,
    pick_random,
    is_empty,
    is_numeric,
    capitalize_text,
    to_uppercase,
    to_lowercase,
)

class TestSaidLangRuntime(unittest.TestCase):
    def test_file_io(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = os.path.join(tmpdir, "test.txt")
            write_file(test_file, "Hello SaidLang")
            self.assertEqual(read_file(test_file), "Hello SaidLang")
            append_file(test_file, "\nSecond Line")
            self.assertEqual(read_file(test_file), "Hello SaidLang\nSecond Line")

    def test_random_helpers(self):
        val = random_number(1, 10)
        self.assertTrue(1 <= val <= 10)
        items = ["apple", "banana", "cherry"]
        chosen = pick_random(items)
        self.assertIn(chosen, items)

    def test_string_helpers(self):
        self.assertTrue(is_empty(""))
        self.assertFalse(is_empty("text"))
        self.assertTrue(is_numeric("123"))
        self.assertFalse(is_numeric("abc"))
        self.assertEqual(capitalize_text("hello"), "Hello")
        self.assertEqual(to_uppercase("hello"), "HELLO")
        self.assertEqual(to_lowercase("HELLO"), "hello")

if __name__ == '__main__':
    unittest.main()
