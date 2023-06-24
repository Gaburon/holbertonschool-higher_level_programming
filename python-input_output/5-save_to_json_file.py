#!/usr/bin/python3
"""
    Module to write from an object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
        save_to_json_file - writes my_obj to file filename
    """
    with open(filename, encoding='utf-8', mode='w') as file:
        file.write(json.dumps(my_obj))
