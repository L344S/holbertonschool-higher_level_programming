#!/usr/bin/python3
"""Tests for the Base, Rectangle and Square classes"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def test_id(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base(3)
        self.assertEqual(base3.id, 3)
