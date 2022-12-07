#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_total = 0
    for index, number in enumerate(my_list):
        if my_list.index(number) == index:
            unique_total += number
    return unique_total
