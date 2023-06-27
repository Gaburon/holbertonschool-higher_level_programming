#!/usr/bin/python3
"""
Module 1-Base_Class
"""


class Base:
    """
    class that will be de base of te other classes
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
