#!/usr/bin/python3
"""
The matrix_mull function
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices(lists of lists of integers/floats)"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    matrix_1 = len(m_a)
    if matrix_1 == 0:
        raise ValueError("m_a can't be empty")
    matrix_2 = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if matrix_2 is None:
           matrix_2 = len(i)
            if matrix_2 == 0:
                raise ValueError("m_a can't be empty")
        if matrix_2 != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    matrix_3 = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if matrix_3 is None:
            matrix_3 = len(i)
            if matrix_3 == 0:
                raise ValueError("m_b can't be empty")
        if matrix_3 != len(i):
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if matrix_2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(l1):
        l = []
        for j in range(l3):
            n = 0
            for k in range(l2):
                n += m_a[i][k] * m_b[k][j]
            matrix.append(n)
        matrix.append(matrix)
    return matrix
