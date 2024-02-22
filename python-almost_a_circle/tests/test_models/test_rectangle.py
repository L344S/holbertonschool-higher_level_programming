#!/usr/bin/python3
"""Tests for the Base class"""
import sys
import unittest
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class"""

    def test_rectangle_creation_1(self):  # Base case for rectangle creation
        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)

    def test_rectangle_creation_2(self):  # Test for width, height, x
        rectangle = Rectangle(1, 2, 3)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)

    def test_rectangle_creation_3(self):  # Test for width, height, x, y
        rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_rectangle_creation_4(self):  # Test for width, height, x, y, id
        rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)
        self.assertEqual(rectangle.id, 5)

    def test_type(self):  # Test if typeError is raised when needed
        self.assertRaises(TypeError, Rectangle, "1", 1)
        self.assertRaises(TypeError, Rectangle, width='2')
        self.assertRaises(TypeError, Rectangle, width=float('NaN'))
        self.assertRaises(TypeError, Rectangle, width=float('inf'))
        self.assertRaises(TypeError, Rectangle, 1, height='abc')
        self.assertRaises(TypeError, Rectangle, 1, 1, x={})
        self.assertRaises(TypeError, Rectangle, 1, 1, y=2.5)

    def test_value(self):  # Test if valueError is raised when needed
        self.assertRaises(ValueError, Rectangle, -5, 1)
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, -565)
        self.assertRaises(ValueError, Rectangle, 1, 1, -755)
        self.assertRaises(ValueError, Rectangle, 1, 1, -2)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

    def test_area(self):  # Test for area method
        rectangle = Rectangle(6, 2)
        self.assertEqual(rectangle.area(), 12)

    def test_rectangle_str(self):  # Test for __str__ method
        rectangle = Rectangle(1, 2, 3, 4, 5)
        expected_str = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(str(rectangle), expected_str)

    def test_display_without_x_y(self):  # Test for display method
        rectangle = Rectangle(2, 2)
        expected_output = "##\n##\n"
        old_stdout = sys.stdout
        # Redirect stdout temporarily to object StringIO
        sys.stdout = mystdout = StringIO()
        rectangle.display()
        sys.stdout = old_stdout  # Put the orginal stdout back
        # Compare the output store in StringIO object with expected output
        self.assertEqual(mystdout.getvalue(), expected_output)
