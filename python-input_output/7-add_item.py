#!/usr/bin/python3

""" This module writes a script that adds all arguments to a Python list,
and then save them to a file.
You must use your function save_to_json_file from 5-save_to_json_file.py.
You must use your function load_from_json_file from 6-load_from_json_file.py.
The list must be saved as a JSON representation in a file named add_item.json.
If the file doesn’t exist, it should be created
Does not manage file permissions / exceptions.
"""


import sys
from typing import List
import importlib

# Use importlib to import modules with non-standard names
save_to_json_file = (
    importlib.import_module('5-save_to_json_file').save_to_json_file
)
load_from_json_file = (
    importlib.import_module('6-load_from_json_file').load_from_json_file
)


def add_items_to_list(args: List[str]):
    """ script that adds all arguments to a Python list,
and then save them to a file.

    Args:
        args (List[str]): args are key to a list of strings
    """
    try:
        # Load existing items from file, if it exists
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If file doesn't exist, start with an empty list
        items = []

    # Add new items to the list
    items.extend(args)

    # Save the updated list to file
    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":
    # Remove the script name from arguments
    arguments = sys.argv[1:]
    add_items_to_list(arguments)
    