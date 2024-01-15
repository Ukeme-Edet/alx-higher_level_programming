#!/usr/bin/python3
"""Unittest for models/rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class"""

    def setUp(self):
        """Set up for all methods"""
        Rectangle._Base__nb_objects = 0

    def test_id(self):
        """Test id attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r4.id, 0)

    def test_width(self):
        """Test width attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        r4 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r4.width, 10)

    def test_height(self):
        """Test height attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.height, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.height, 2)
        r4 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r4.height, 2)

    def test_x(self):
        """Test x attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)
        r2 = Rectangle(2, 10, 3)
        self.assertEqual(r2.x, 3)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.x, 0)
        r4 = Rectangle(10, 2, 3, 0, 0)
        self.assertEqual(r4.x, 3)
        r5 = Rectangle(10, 2, -3, 0, 0)
        self.assertEqual(r5.x, -3)

    def test_y(self):
        """Test y attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 10, 3)
        self.assertEqual(r2.y, 0)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.y, 0)
        r4 = Rectangle(10, 2, 3, 0, 0)
        self.assertEqual(r4.y, 0)
        r5 = Rectangle(10, 2, -3, 0, 0)
        self.assertEqual(r5.y, 0)

    def test_width_TypeError(self):
        """Test width TypeError"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('-inf'), 10)

    def test_height_TypeError(self):
        """Test height TypeError"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, True)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, (1, 2))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {"a": 1, "b": 2})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float('nan'))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float('inf'))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float('-inf'))

    def test_x_TypeError(self):
        """Test x TypeError"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, (1, 2))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {"a": 1, "b": 2})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, float('nan'))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, float('inf'))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, float('-inf'))

    def test_y_TypeError(self):
        """Test y TypeError"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "4")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, (1, 2))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, {"a": 1, "b": 2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, float('nan'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, float('inf'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, float('-inf'))

    def test_width_ValueError(self):
        """Test width ValueError"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2, 3)

    def test_height_ValueError(self):
        """Test height ValueError"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2, 3)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0, 3)

    def test_x_ValueError(self):
        """Test x ValueError"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3, 4)

    def test_y_ValueError(self):
        """Test y ValueError"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -4, 5)


if __name__ == '__main__':
    unittest.main()
