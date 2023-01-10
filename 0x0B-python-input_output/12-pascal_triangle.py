#!/usr/bin/python3
"""Pascal trinagle module"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    outer_list = []
    for i in range(n):
        if len(outer_list) == 0:
            outer_list.append([1])
            continue
        if len(outer_list) == 1:
            outer_list.append([1, 1])
            continue
        prev_list = outer_list[len(outer_list) - 1]
        next_list = []
        first_item = 1
        for index, num in enumerate(prev_list):
            if first_item:
                next_list.append(num)
                first_item = 0
            else:
                if index + 1 != len(prev_list):
                    next_list.append(prev_list[index - 1] + prev_list[index])
                else:
                    next_list.append(prev_list[index - 1] + prev_list[index])
                    next_list.append(prev_list[index])
        outer_list.append(next_list)

    return outer_list
