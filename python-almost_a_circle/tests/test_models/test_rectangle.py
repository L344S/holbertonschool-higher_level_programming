#!/usr/bin/python3
"""Tests for the Rectancle class"""
import os
import json
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

    # Test for display method with w, h and x
    def test_display_without_y(self):
        rectangle = Rectangle(2, 2, 2)
        expected_output = "  ##\n  ##\n"
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        rectangle.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), expected_output)

    def test_display(self):  # Test for display method with w, h, x and y
        rectangle = Rectangle(2, 2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        rectangle.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), expected_output)

    def test_display_exist(self):
        rectangle = Rectangle(2, 4, 1, 2)
        expected_output = "\n\n ##\n ##\n ##\n ##\n"
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        rectangle.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), expected_output)

    def test_update(self):
        rectangle = Rectangle(1, 1)
        rectangle.update(89, 1, 2, 3, 4)
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_to_dictionary(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        expected_dict = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)

    def test_create_without_x_y(self):
        rectangle = Rectangle.create(**{'id': 1, 'width': 2, 'height': 3})
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)

    def test_create_withouth_y(self):
        rectangle = Rectangle.create(
            **{'id': 1, 'width': 2, 'height': 3, 'x': 4})
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 4)

    def test_create_with_all_args(self):
        rectangle = Rectangle.create(
            **{'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5})
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

    def test_save_to_file_NONE(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            content = file.read()
        expected_output = '[]'
        self.assertEqual(content, expected_output)
        os.remove("Rectangle.json")

    def test_save_to_fempty(self):
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_save_and_load(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([rectangle])
        loaded = Rectangle.load_from_file()
        self.assertEqual(loaded[0].id, 5)
        self.assertEqual(loaded[0].width, 1)
        self.assertEqual(loaded[0].height, 2)
        self.assertEqual(loaded[0].x, 3)
        self.assertEqual(loaded[0].y, 4)

    def test_load_from_file_not_exist(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])
