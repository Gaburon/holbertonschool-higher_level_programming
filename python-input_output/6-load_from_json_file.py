#!/usr/bin/python3
"""
    Module to create from JSON
"""


def load_from_json_file(filename):
    """
        creates an Object from a “JSON file”
    """
    import json

    with open(filename, encoding='utf-8') as file:
        return json.load(file)
