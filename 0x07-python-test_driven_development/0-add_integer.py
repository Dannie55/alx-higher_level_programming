#!/usr/bin/python3
"""
Module for ""0-add_integer".

The 0-add_integer module returns the function add integer(a,b)
"""


def add_integer(a, b=98):
    """Return the sum of two numbers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type a is a float:
        a = int(a)
    if type b is a float:
        b = int(b)
    return a + b
