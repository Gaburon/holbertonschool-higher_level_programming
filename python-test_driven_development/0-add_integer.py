#!/usr/bin/python3
"""
Definning a funtion wich adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Arguments:
        Datatypes
    Raises:
        TypeError (a): Must be an integer.
        TypeError (b): Must be an integer.
    Returns:
        Sum of the two integers.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
