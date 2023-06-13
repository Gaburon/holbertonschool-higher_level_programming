#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """initialize size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size <= 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
