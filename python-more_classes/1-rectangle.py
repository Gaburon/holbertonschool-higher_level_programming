#!/usr/bin/python3
"""
Definning a Rectangle class
"""


class Rectangle:
    """
    Definning a Rectangle class.
    """

    def __init__(self, width=0, height=0):
        """
        Initializing Nwe rectangle
        Arguments:
        width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Setting the width of the new rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Setting the height of the new rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
