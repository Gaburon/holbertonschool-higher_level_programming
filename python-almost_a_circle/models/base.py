#!/usr/bin/python3
"""
Module 1-Base_Class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        classmethod that writes the JSON string representation
        of list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = class_name + ".json"
        result = []

        for obj in list_objs:
            result.append(cls.to_dictionary(obj))

        json_string = Base.to_json_string(result)

        with open(filename, mode="w", encoding="UTF-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns the list of the JSON
        string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
