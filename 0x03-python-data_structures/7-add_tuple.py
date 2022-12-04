#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    [a1, a2] = assign_val(tuple_a)
    [b1, b2] = assign_val(tuple_b)
    new_tuple = (a1 + b1, a2 + b2)
    return new_tuple


def assign_val(_tuple):
    if len(_tuple) == 0:
        return [0, 0]
    if len(_tuple) == 1:
        return [_tuple[0], 0]
    return [_tuple[0], _tuple[1]]
