#!/usr/bin/python3
"""Defines a class and inheritance of a class"""


def is_kind_of_class(obj, a_class):
    """Returns true if an object is an instance of an inherited class
    Args:
        obj(any): object to be checked.
        a_class(type): The class to match the object to
    Return:
         if an obj is an instance or inherited instance of a class -True
        Otherwise return -False.
    """
    if isinstance(obj, a_class):
        return True
    return False
