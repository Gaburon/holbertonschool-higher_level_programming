#!/usr/bin/python3

"""Defines clase Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Initializes square class
    """
    def __init__(self, size):
        """
        size initializer
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Area of square
        """
        return self.__size * self.__size
