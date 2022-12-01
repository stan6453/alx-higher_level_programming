#!/usr/bin/python3

import dis
import marshal

f = open("hidden_4.pyc", "rb")
f.read(16)

code = marshal.load(f)
consts = []
count = 1
for item in code.co_consts:
    not_in = item not in ("__init__", None)
    if count % 2 == 0 and not_in:
        consts.append(item)
    count = count + 1
consts.sort()
for string in consts:
    if __name__ == '__main__':
        print(string)
