#!/usr/bin/python3
def remove_char_at(str1, n):
    if n > len(str1) or n < 0:
        return str1
    mylist = [""] * (len(str1) - 1)
    list_index = 0
    for str_index in range(len(str1)):
        if str_index != n:
            mylist[list_index] = str1[str_index]
            list_index = list_index + 1
    return "".join(mylist)
