#!/usr/bin/python3

"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""
    pass

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method:  that validates value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
