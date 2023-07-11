#!/usr/bin/python3
"""Defines append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert text after each line containing a given string in a file.
    """
    text = ""
    with open(filename) as rf:
        for line in rf:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as wf:
        wf.write(text)
