#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittest for max_integer([...])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittest for max_integer([...])"""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list beginning with max integer."""
        max_at_beginning = [4, 2, 1, 3]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element(self):
        """Test for one element in list."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test for floats integers."""
        floats = [15.2, 12.0, 0.56, -9.4, 4.7]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test for a combination of ints and floats."""
        int_and_floats = [15.5, -9, 10.4, 12, 15]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test for string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test for list of strings."""
        list_of_strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(list_of_strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
