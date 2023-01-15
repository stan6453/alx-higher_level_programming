#!/usr/bin/python3
"""Test for the Base class to make sure it functions as expected"""

from unittest import TestCase
from models.base import Base

class TestBase(TestCase):
    """Unit test for Base class"""
    def test_id(self):
        obj = Base()
        self.assertEqual(obj.id, 1)
        obj2 = Base()
        self.assertEqual(obj2.id, 2)
        obj3 = Base(7)
        self.assertEqual(obj3.id, 7)
