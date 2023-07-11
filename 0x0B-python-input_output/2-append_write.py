#!/usr/bin/python3
"""Defines write_file function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.app(text)
