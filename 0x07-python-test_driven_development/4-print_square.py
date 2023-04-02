#!/usr/bin/python3
"""
A module for "4-print_square".

The 4-print_square module supplies the print_square(size) function
"""


def print_square(size):
    """Prints a square with ""#""'s that length size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end=" ")
