#!/usr/bin/python3
"""Tests for the Square class"""
import os
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class"""

    """-------- BASECASES --------"""
    def test_Square_without_x_y(self):
        square = Square(1)
        self.assertEqual(square.size, 1)

    def test_Square_without_y(self):
        square = Square(1, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_Square_without_id(self):
        square = Square(1, 2, 3)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_Square_with_all(self):
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)

    """-------- TYPE ERROR --------"""
    def test_Square_size_type(self):
        with self.assertRaises(TypeError):
            square = Square("1")

    def test_Square_x_type(self):
        with self.assertRaises(TypeError):
            square = Square(1, "2")

    def test_Square_y_type(self):
        with self.assertRaises(TypeError):
            square = Square(1, 2, "3")

    """-------- VALUE ERROR --------"""
    def test_Square_size_value(self):
        with self.assertRaises(ValueError):
            square = Square(-1)

    def test_Square_x_value(self):
        with self.assertRaises(ValueError):
            square = Square(1, -2)

    def test_Square_y_value(self):
        with self.assertRaises(ValueError):
            square = Square(1, 2, -3)
    
    def test_Square_size_value_0(self):
        with self.assertRaises(ValueError):
            square = Square(0)
