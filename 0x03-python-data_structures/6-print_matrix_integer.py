#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list1 in matrix:
        for element in list1:
            print("{:2d}".format(element), end="")
        print()
