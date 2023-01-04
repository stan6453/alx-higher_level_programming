#!/usr/bin/python3
"""Matrix module."""


def matrix_divided(matrix, div):
    """Divides a matrix."""
    """Tests."""
    rowlength = None
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    for list1 in matrix:
        if type(list1) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        for number in list1:
            if type(number) is not int:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if rowlength is None:
            rowlength = len(list1)
        else:
            if rowlength != len(list1):
                raise TypeError("Each row of the matrix must have \
the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """code that does actual work"""
    return [[round(number/div, 2) for number in list1] for list1 in matrix]
