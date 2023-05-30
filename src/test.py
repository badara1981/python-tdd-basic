
import unittest

from text import to_upper, to_word_list_isupper


# Task 1
class TestIsUpper(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(to_upper("abcdef"), "ABCDEF")
# Task2

    def test_is_true(self):
        self.assertTrue(to_word_list_isupper(["I", "LOVE", "YOU"]))


# Task3

    def test_is_false(self):
        self.assertFalse(to_word_list_isupper(["i", "LOVE", "YOU"]))


# Task4

    def test_type_str(self):
        with self.assertRaises(TypeError):
            to_upper(800)


# Task5

    def test_type_lst(self):
        with self.assertRaises(TypeError):
            to_word_list_isupper(800)


if __name__ == "__main__":
    unittest.main()