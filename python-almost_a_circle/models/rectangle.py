#!/usr/bin/python3
"""
Module 2-Rectangle
"""

from models.base import Base
"""
Importing Base Class to be inherited
"""


class Rectangle(Base):
    """
    Class Rectangle that inherit from Base Class

    Private Attributes:
        width
        height
        x
        y
    Each one of these have their own getter and setter
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for an instance of the class Rectangle

        Args:
            width
            height
            x
            y
            id - comes from the Super Class Base

        Methods:
            area: returns the area of the object rectangle
            display: prints in stdo the rectangle using '#'
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Setter for width

        Args:
            width
        width must be an int > 0
        """
        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Setter for height

        Args:
            height
        height must be an int > 0
        """
        self.__height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Setter for x

        Args:
            x
        x must be an int >= 0
        """
        self.__x = x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Setter for y

        Args:
            y
        y must be an int >= 0
        """
        self.__y = y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """
        method to return the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        method that prints in stdout the rectangle with the character #
        """
        for a in range(self.y):
            print()
        for i in range(self.__height):
            for b in range(self.x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """
        overriding the __str__ method so that it returns a specific messages
        """
        msg = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                      self.width, self.height)
        return msg
