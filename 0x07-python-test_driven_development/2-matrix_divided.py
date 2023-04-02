#!/usr/bin/python3
"""
A module for ""2-matrix-divided".

This module supplies the function matrix_divided(matrix, divide)
"""


def matrix_divided(matrix, div):
    """Divides all elements in a matrix"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix(list of lists) of integers/floats")
    if not all (len(row) == len(matrix[0] for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div,(int,float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZerroDivisonError("Divison by zero")
    new_matrix = [[round(element/div, 2) for elem in row] for row in matrix]
    return new_matrix
