#!/usr/bin/python3
"""
Definning a function which divises a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix.
    Arguments:
        DataTypes.
    Raises:
        TypeError        (matrix): Matrix must be a matrix (lists of lists)(...).
        TypeError (len of matrix): Each row of the matrix must have the(...).
        TypeError           (div): div must be a number(...).
        ZeroDivisionError   (/ 0): division by zero.
    Returns:
        Division of the matrix.
    """
    if isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
