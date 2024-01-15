#!/usr/bin/python3
"""Unittest for models/base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for Base class"""

    def setUp(self):
        """Set up for all methods"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)


if __name__ == "__main__":
    unittest.main()
