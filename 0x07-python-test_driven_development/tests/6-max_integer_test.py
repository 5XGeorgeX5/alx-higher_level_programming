#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_list(self):
        """Test a list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, -2, 4, 3]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([7]), 7)

    def test_list_with_floats(self):
        """Test a list includes floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        self.assertEqual(max_integer("George"), 'r')
        self.assertEqual(max_integer(""), None)

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["George", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

if __name__ == '__main__':
    unittest.main()
