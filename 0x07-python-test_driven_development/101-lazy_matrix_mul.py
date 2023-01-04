#!/usr/bin/python3
"""Matrix multiplication module."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiply two matrices"""

    """Tests"""
    list_list_of_numbers(m_a, "m_a")
    list_list_of_numbers(m_b, "m_b")
    can_multiply(m_a, m_b)

    """Code that does actual work"""
    return np.matmul(m_a, m_b)


def list_list_of_numbers(matrix, name):
    """make sure matrix is a list of list of integers or float."""
    rowlength = None
    if type(matrix) is not list:
        raise TypeError("{} must be a list".format(name))

    if not matrix or len(matrix) == 1 and not matrix[0]:
        raise ValueError("{} can't be empty".format(name))

    for row in matrix:
        if type(row) is not list:
            raise TypeError("{} must be a list of lists".format(name))
        for number in row:
            if type(number) not in [int, float]:
                raise TypeError("{} should contain only \
integers or floats".format(name))
        if rowlength is None:
            rowlength = len(row)
        else:
            if rowlength != len(row):
                raise TypeError("each row of {} must \
be of the same size".format(name))


def can_multiply(m_a, m_b):
    a_rowlength = len(m_a[0])
    b_columnlength = len(m_b)

    if a_rowlength != b_columnlength:
        raise ValueError("m_a and m_b can't be multiplied")
