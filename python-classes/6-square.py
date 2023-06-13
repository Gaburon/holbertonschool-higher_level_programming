#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Size - Square size"""
        return self.__size

    """Size setter"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """position - (x, y) to print square"""
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self):
        if isinstance(value, tuple) is False or len(value) != 2\
                or isinstance(value[0], int) is False\
                or isinstance(value[1], int) is False\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value

    """return the area of the square"""
    def area(self):
        return self.__size**2

    """Prints square"""
    def my_print(self):
        if self.size == 0:
            print()
        else:
            for y in range(self.position[1]):
                print()
            for height in range(self.size):
                for x in range(self.position[0]):
                    print(" ", end="")
                for length in range(self.size):
                    print("#", end="")
            print()
