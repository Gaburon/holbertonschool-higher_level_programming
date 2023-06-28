#!/usr/bin/python3
"""
Unittest for Rectangle Class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """
    unittests for functions in Rectangle Class
    """

    def test_ints(self):
        r1 = Rectangle(5, 6)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 6)

        r2 = Rectangle(6, 5)
        self.assertEqual(r2.width, 6)
        self.assertEqual(r2.height, 5)

        r3 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
        self.assertEqual(r3.id, 5)

    def test_arg_type(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, [2], 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, {"k": 4}, 5)
        with self.assertRaises(TypeError):
            Rectangle((1, 2), 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "Holberton", 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, {4}, 5)

    def test_arg_value(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            Rectangle(1, 0, 3, 4, 5)
        with self.assertRaises(ValueError):
            Rectangle(1, -2, 3, 4, 5)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2, -3, 4, 5)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4, 5)

    def test_area(self):
        r4 = Rectangle(3, 2)
        self.assertEqual(r4.area(), 6)

        r5 = Rectangle(2, 10)
        self.assertEqual(r5.area(), 20)

        r6 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r6.area(), 56)

    def test_str_format(self):
        r7 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r7.__str__(), "[Rectangle] (5) 3/4 - 1/2")

    if __name__ == '__main__':
        unittest.main()
