#!/usr/bin/python3
"""Defines a class inherited directly of indirectly from a specified class"""


def inherits_from(obj, a_class):
    """Returns true if inherited directly or indirectly from a specified class
    Args:
        obj(any): The object of a class.
        a_class(type): matched to the object
    Returns:
        if the obj is  inherited directly or indirectly - True
        Otherwise return- False.
    """
    if issubclass(type(obj), a_class):
        return True
    return False
