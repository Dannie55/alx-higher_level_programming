#!/usr/bin/python3
"""
Module for "3-say_my_name".

The 3-say_my_name module supplies say_my_name function.
"""


def say_my_name(first_name, last_name=""):
    """Prints "My name" is followed by first name and lastly last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not a str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
