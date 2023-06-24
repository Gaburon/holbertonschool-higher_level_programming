#!/usr/bin/python3
"""
Definning a file writing function.
"""


def write_file(filename="", text=""):
    """
    Write a string into a UTF8 File.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
