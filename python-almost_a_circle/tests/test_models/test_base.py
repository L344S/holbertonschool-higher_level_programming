#!/usr/bin/python3
"""Test for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def test_id(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base(125)
        self.assertEqual(base3.id, 125)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), '[]')
