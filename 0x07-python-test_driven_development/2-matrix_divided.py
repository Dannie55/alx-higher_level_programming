#!/usr/bin/python3
"""
A module for ""2-matrix-divided".

This module 2-matrix-divided supplies the function matrix_divided(matrix, divide)
"""


def matrix_divided(matrix, div):
    """Divides all elements in a matrix"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix(list of lists) of integers/floats")
    size = None
    for row in matrix:
        if type(row) is not a list:
            raise TypeError("matrix must be matrix (list of lists) of integers/floats")
        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]
