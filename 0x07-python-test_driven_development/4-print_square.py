#!/usr/bin/python3
"""Defines a print_square function."""


def print_square(size):
    """
    Print a square.
    Args:
        size (int): The square size.
    Raises:
        TypeError: If size is not int.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
