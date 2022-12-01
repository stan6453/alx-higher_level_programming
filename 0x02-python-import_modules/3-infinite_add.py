#!/usr/bin/python3

from sys import argv

total = 0
if len(argv) > 1:
    for index in range(1, len(argv)):
       total += int(argv[index])

print(total)
