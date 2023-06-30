#!/usr/bin/python3
"""Defines a text_indentation function."""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    len1 = len(text)

    c = 0
    while c < len1 and text[c] == ' ':
        c += 1

    while c < len1:
        print(text[c], end="")
        if text[c] in ".?:\n":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len1 and text[c] == ' ':
                c += 1
            continue
        c += 1
