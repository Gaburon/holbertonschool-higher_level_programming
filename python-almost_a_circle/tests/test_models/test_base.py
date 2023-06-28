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


if __name__ == '__main__':
    unittest.main()
