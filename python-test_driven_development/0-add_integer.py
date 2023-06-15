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

    if (type(a) != int and (type(a) != float)):
        raise TypeError ("a must be an integer")
    if (type(b) != int and (type(b) != float)):
        raise TypeError ("b must be an integer")
    
    return int(a) + int(b)