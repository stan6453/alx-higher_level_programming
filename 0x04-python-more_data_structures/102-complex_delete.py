#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return a_dictionary
    keys = a_dictionary.copy().keys()
    values = a_dictionary.copy().values()
    for key, value1 in zip(keys, values):
        if value1 == value:
            a_dictionary.pop(key)
    return a_dictionary
