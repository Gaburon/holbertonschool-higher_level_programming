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

    def area(self):
        """
        Returns the perimeter of the rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Return the perimeter
        """
        if self.__height == 0 or self.width == 0:
            return (0)
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Return rectangles graphical representation
        """
        str = ""
        if self.__width == 0 or self.__height == 0:
            return (0)
        for i in range(0, self.height):
            for j in range(0, self.width):
                str = str + "#"
            str = str + "\n"
        str = str[0:-1]
        return(str)

    def __repr__(self):
        """
        Return the string representation of the rectangle
        """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
