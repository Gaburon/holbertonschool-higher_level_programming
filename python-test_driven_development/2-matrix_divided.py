#!/usr/bin/python3
"""
Definning a function which divises a matrix.
"""


def matrix_divided(matrix, div):
    """ divides all elemnts of a matrix"""

    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    for array in matrix:
        for element in array:
            if type(element) not in [int, float]
            raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats")
        if type(div) not in [int, float]:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
