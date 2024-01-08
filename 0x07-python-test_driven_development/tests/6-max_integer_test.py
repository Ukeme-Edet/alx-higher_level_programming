#!/usr/bin/env python3
"""Unit test for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    A class to test the max_integer function.
    """

    def test_max_integer(self):
        """
        Test the max_integer function with a list of integers.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([]), None)
