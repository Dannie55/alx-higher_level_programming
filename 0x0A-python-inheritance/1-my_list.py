#!/usr/bin/python3
"""Defines a list that inherit from MyList"""


class MyList(list):
    """implements sorted printing for the built in class list"""
    def print_sorted(self):
        """prints a list in ascending order"""
        print(sorted(self))
