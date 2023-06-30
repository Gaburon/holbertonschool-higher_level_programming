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

    def test_from_jsoon_string(self):
        json_str = None
        self.assertEqual(Base.from_json_string(json_str), [])

        json_str = '[]'
        self.assertEqual(Base.from_json_string(json_str), [])

        json_str = '[{"id": 14}]'
        self.assertEqual(Base.from_json_string(json_str), [{'id': 14}])

    def test_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()),
                             [r1.to_dictionary(), r2.to_dictionary()])
        os.remove("Rectangle.json")

     def test_create(self):
        """Test create method"""
        r1 = Rectangle(3, 5, 7, 9, 12)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)

    def test_load_from_file(self):
        """Test load_from_file method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 3)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertTrue(all(isinstance(i, Rectangle)
                            for i in list_rectangles_output))

        self.assertTrue(all(hasattr(i, 'width')
                            for i in list_rectangles_output))

        self.assertTrue(all(hasattr(i, 'height')
                            for i in list_rectangles_output))

        self.assertTrue(all(hasattr(i, 'x')
                            for i in list_rectangles_output))

        self.assertTrue(all(hasattr(i, 'y')
                            for i in list_rectangles_output))

        self.assertTrue(all(hasattr(i, 'id')
                            for i in list_rectangles_output))

        os.remove("Rectangle.json")


if __name__ == '__main__':
    unittest.main()
