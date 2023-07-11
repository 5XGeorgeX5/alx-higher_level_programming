#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save1 = __import__('5-save_to_json_file').save_to_json_file
    load1 = __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load1("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save1(items, "add_item.json")
