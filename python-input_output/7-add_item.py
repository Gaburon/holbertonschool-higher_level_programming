#!/usr/bin/python3
"""Add its arguments to a python list"""
import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

try:
    Items = load("add_item.json")
except FileNotFoundError:
    Items = []

Items += sys.argv[1:]
save(Items, "add_item.json")
