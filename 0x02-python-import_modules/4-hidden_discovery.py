#!/usr/bin/python3

import dis
import marshal

f = open("hidden_4.pyc", "rb")
f.read(16)

code = marshal.load(f)
consts = []
for item in code.co_consts:
    not_in = itme not in ("__init__", None)
    if type(item) != type(code.co_consts[0]) and not_in:
        consts.append(item)

consts.sort()
for string in consts:
    print(string)
