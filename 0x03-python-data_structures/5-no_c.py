#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return
    new_str = ""
    for letter in my_string:
        if letter != 'C' and letter != 'c':
            new_str = new_str + letter
    return new_str
