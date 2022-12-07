#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda list1: list(map(lambda x: x**2, list1)), matrix))
