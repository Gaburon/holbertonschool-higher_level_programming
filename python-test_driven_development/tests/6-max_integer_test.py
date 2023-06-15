#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        # Test max_integer with some lists
        self.assertEqual(max_integer([1, 4, 8]), 8)
        self.assertEqual(max_integer([-2, -8, -1]), -1)
        self.assertEqual(max_integer([2, 2, 3, 3]), 3)
        self.assertEqual(max_integer(), None)

    def test_type(self):
        # Test max_integer with wrong types
        self.assertEqual(max_integer("Hello world"), 'w')
        self.assertRaises(TypeError, max_integer, ['a', 3, 9])
        self.assertEqual(max_integer([3.1, 4.8, 9.62]), 9.62)
        self.assertEqual(max_integer([[2], [3], [6]]), [6])
