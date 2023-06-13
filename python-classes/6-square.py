#!/usr/bin/python3
""" Square - First python classes's class """


class Square:
    """ Init method to instiantiate """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Size - Square's size """
        return self._size

    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    @property
    def position(self):
        """ Position - (x, y) tuple to print the square on """
        return self._position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is False or len(value) != 2\
                or isinstance(value[0], int) is False\
                or isinstance(value[1], int) is False\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value

    """ Area - Calcs the area of the square """
    def area(self):
        area = self.size ** 2
        return area

    """ My print - Prints the square using # at given position """
    def my_print(self):
        if (self.size == 0):
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
