#!/usr/bin/python3
""" Add integer
    This modlue adds two numbers"""


def add_integer(a, b=98):
    """ Argumens:
        a: first number to add
        b: second number to add

        Returns:
            int: the sum of bot numbers casted to integers
            Typerror if a or b is not a number
    """

    if isinstance(a, int) is False and isinstance(a, float) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) is False and isinstance(b, float) is False:
        raise TypeError("b must be an integer")
    return int(a) + int
