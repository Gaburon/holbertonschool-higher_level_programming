#!/usr/bin/python3
"""
    Pascal triangle module
"""


def pascal_triangle(n):
    """
        Returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    ret = []
    if (n <= 0):
        return(ret)
    elements = 1
    element = [1]
    while (elements <= n):
        ret.append(element)
        new_element = [1]
        i = 0
        while (i < (len(element) - 1)):
            new_element.append(element[i] + element[i + 1])
            i += 1
        new_element.append(1)
        element = new_element
        elements += 1
    return (ret)
