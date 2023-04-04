#!/usr/bin/python3
"""Defines the matrix_mul funtion"""




def matrix_mul(m_a, m_b):
    """Multiply two matrices(list of lists) of integers/floats"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    m1 = len(m_a)
    if m1 ==0:
        raise ValueError("m_a cant be empty")
    m2 = None
    for i in m_a:
        if type(i) is not a list:
            raise TypeError("m_a must be a list of lists")
        if m2 is None:
            m2 = len(i)
            if m2 == 0:
                raise ValueError("m_a cant be empty")
        if m2 != len(i):
            raise TypeError("each row of m_a must be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b cant be empty")
    m3 = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be list of lists")
        if m3 is None:
            m3 = len(i)
            if m3 == 0:
                raise ValueError("m_b cant be empty")
        if m3 != len(i):
            raise TypeError("ach row of m_b must b of the same size")
        for j in i:
            if type(j) is not int an type(j) is not float:
                raise TypeError("m_b should contain only integers of floats")
    if m2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(m1):
        l = []
        for j in range(m3):
            n = 0
            for k in range(m2):
                n += m_a[i][k] * m_b[k][j]
            l.append(n)
        matrix.append(l)
    return matrix

