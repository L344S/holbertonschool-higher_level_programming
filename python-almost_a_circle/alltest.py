#!/usr/bin/python3
"""Tests for the Base, Rectangle and Square classes"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

"""------------------- TestBase -------------------"""
class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def test_assign_id(self):
        test = Base(50)
        self.assertEqual(test.id, 50)

    def test_no_id_assigned(self):
        test = Base()
        self.assertEqual(test.id, 1)

    def test_to_json_string(self):
        dictionary = {'id': 50,
                      'width': 10,
                      'height': 5,
                      'x': 2,
                      'y': 3}
        json_string = Base.to_json_string(dictionary)
        self.assertTrue(isinstance(json_string, str))

    def test_to_json_string_content(self):
        dictionary = {'id': 50,
                      'width': 10,
                      'height': 5,
                      'x': 2,
                      'y': 3}
        json_string = Base.to_json_string(dictionary)
        self.assertCountEqual(json.loads(json_string), dictionary)
    
    def test_to_json_string_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json.loads(json_string), [])

    def test_from_json_string(self):
        string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        json_list = Base.from_json_string(string)
        self.assertTrue(isinstance(json_list, list))

    def test_from_json_string_content(self):
        string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        expected_list = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}]
        json_list = Base.from_json_string(string)
        self.assertEqual(json_list, expected_list)

    def test_from_json_string_none(self):
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])

"""------------------- TestSquare -------------------"""
class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class"""
    def test_rectangle_init(self):
        rectangle = Rectangle(3, 2)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 2)

    def test_rectangle_init_with_pos(self):
        rectangle = Rectangle(3, 2, 1)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 0)

    def test_rectangle_init_with_id(self):
        rectangle = Rectangle(3, 2, 1, 0, 10)
        self.assertEqual(rectangle.id, 10)

    def test_rectangle_int_error(self):
        with self.assertRaises(TypeError) as err:
            rectangle = Rectangle("hello", 2, 3)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_rectangle_value_error(self):
        with self.assertRaises(ValueError) as err:
            rectangle = Rectangle(-2, 1)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_rectangle_area(self):
        rectangle = Rectangle(3, 2)
        self.assertEqual(rectangle.area(), 6)

    def test_rectangle_str(self):
        rectangle = Rectangle(3, 2, 1, 0, 10)
        expected_output = "[Rectangle] (10) 1/0 - 3/2"
        self.assertEqual(str(rectangle), expected_output)

    def test_rectangle_update(self):
        rectangle = Rectangle(3, 2, 1, 0, 10)
        rectangle.update(25, 30, 20, 0, 1)
        self.assertEqual(rectangle.width, 30)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 1)
        self.assertEqual(rectangle.id, 25)

    def test_rectangle_update_kwargs(self):
        rectangle = Rectangle(3, 2, 1, 0, 10)
        rectangle.update(height=10)
        self.assertEqual(rectangle.height, 10)

    def test_rectangle_to_dictionary(self):
        rectangle = Rectangle(3, 2, 1, 0, 10)
        rectangle_dict = rectangle.to_dictionary()
        expected_dict = {'id': 10, 'width': 3, 'height': 2, 'x': 1, 'y': 0}
        self.assertEqual(rectangle_dict, expected_dict)

"""------------------- TestSquare -------------------"""
class TestSquare(unittest.TestCase):
    """Tests for the Square class"""

    def test_square_init(self):
        square = Square(3)
        self.assertEqual(square.size, 3)

    def test_square_init_with_pos(self):
        square = Square(3, 2, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 1)

    def test_square_init_with_id(self):
        square = Square(3, 2, 1, 10)
        self.assertEqual(square.id, 10)

    def test_square_int_error(self):
        with self.assertRaises(TypeError) as err:
            square = Square("hello", 2, 3)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_square_value_error(self):
        with self.assertRaises(ValueError) as err:
            square = Square(-2)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_square_area(self):
        square = Square(3)
        self.assertEqual(square.area(), 9)

    def test_square_str(self):
        square = Square(3, 2, 1, 10)
        expected_output = "[Square] (10) 2/1 - 3"
        self.assertEqual(str(square), expected_output)

    def test_square_update(self):
        square = Square(3, 2, 1, 10)
        square.update(25, 30, 20, 10)
        self.assertEqual(square.size, 30)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 10)
        self.assertEqual(square.id, 25)

    def test_square_update_kwargs(self):
        square = Square(3, 2, 1, 10)
        square.update(size=10)
        self.assertEqual(square.size, 10)

    def test_square_to_dictionary(self):
        square = Square(3, 2, 1, 10)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 10, 'size': 3, 'x': 2, 'y': 1}
        self.assertEqual(square_dict, expected_dict)
