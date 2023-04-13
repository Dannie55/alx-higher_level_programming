#!/usr/bin/python3
"""Defines a txt file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """insert txt after each line that contains a string in a file.
    Args:
         filename (str): The file name.
         search_string (str): The string to search for within the file.
         new_string (str): string to insert
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
