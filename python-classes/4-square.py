#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Size - Square size"""
        return self.size
    """Size setter"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = value
    """return the area of the square"""
    def area(self):
        return self.size**2
