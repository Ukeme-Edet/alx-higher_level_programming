#!/usr/bin/python3
"""Unittest for models/base.py"""
import unittest
from models.base import Base
from models.square import Square


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

    def test_to_json_string(self):
        """Test to_json_string method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')

    def test_save_to_file(self):
        """Test save_to_file method"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        Square.save_to_file([Square(1, 2)])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 1, "size": 1, "x": 2, "y": 0}]')


if __name__ == "__main__":
    unittest.main()
