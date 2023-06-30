#!/usr/bin/python3
"""
    Script to save arguments to a file
"""

import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    arguments = load_from_json_file("add_item.json")
except Exception:
    arguments = []

i = 1
while i < len(sys.argv):
    arguments.append(sys.argv[i])
    i += 1

with open("add_item.json", encoding='utf-8', mode='w') as file:
    file.write(json.dumps(arguments))
