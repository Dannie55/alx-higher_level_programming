#!/usr/bin/python3
"""
A module for "5-text_indentation".

The 5-text_indentation module supplies the text_indentation(text) function.
"""


def text_indentation(text):
    """Splits text into line along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    dance = 0
    for a in text:
        if dance == 0:
            if a == ' ':
                continue
            else:
                dance = 1
        if dance == 1:
            if a == '?' or a == ':' or a == '.':
                print(a)
                print()
                dance = 0
            else:
                print(a, end="")
