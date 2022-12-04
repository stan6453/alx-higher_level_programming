#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for list1 in matrix:
        if not list1:
            continue
        print("{:d} {:2d} {:2d}".format(list1[0],list1[1],list1[2]))
