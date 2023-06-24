#!/usr/bin/python3
"""
Definning a function wich appends a string.
"""
import json


def from_json_string(my_str):
    """
    Returns a obj rep of a JSON String.
    """
    return json.loads(my_str)
