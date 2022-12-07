#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weighted_sum = 0
    num_elem = 0
    for tuple1 in my_list:
        weighted_sum += tuple1[0] * tuple1[1]
        num_elem += tuple1[1]
    return weighted_sum / num_elem
