#!/usr/bin/python3
"""
Unittest for Base Class
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    unittests for functions in Base Class
    """

    def test_empty(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_specific_id(self):
        b2 = Base(14)
        self.assertEqual(b2.id, 14)

    def test_default(self):
        b3 = Base(None)
        self.assertEqual(b3.id, 1)

    def test_to_json_string(self):
        list_dictionaries = [{'i': 1, 'j': 2}, {'x': 3, 'y': 4}]
        self.assertEqual(Base.to_json_string(list_dictionaries),
                         '[{"i": 1, "j": 2}, {"x": 3, "y": 4}]')

        list_dictionaries = []
        self.assertEqual(Base.to_json_string(list_dictionaries), "[]")

        list_dictionaries = None
        self.assertEqual(Base.to_json_string(list_dictionaries), "[]")


if __name__ == '__main__':
    unittest.main()
