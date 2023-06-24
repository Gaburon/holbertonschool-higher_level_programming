#!/usr/bin/python3
"""
Creating a obj from an JSON File.
"""
import json


def load_from_json_file(filename):
    """
    Creating a obj from an JSON File.
    """
    with open(filename) as file:
        return json.load(file)
