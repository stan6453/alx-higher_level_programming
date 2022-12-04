#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list1 in matrix:
        for element in list1:
            if id(element) == id(list1[0]):
                print("{:d}".format(element), end="")
            else:
                print("{:2d}".format(element), end="")
        print()
