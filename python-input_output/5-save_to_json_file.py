#!/usr/bin/python3
"""The onjext is here"""


import json


def save_to_json_file(my_obj, filename):
    """SAVE JASON!!! HE'S NEARING THE ROAD"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (json.dump(my_obj, f))
