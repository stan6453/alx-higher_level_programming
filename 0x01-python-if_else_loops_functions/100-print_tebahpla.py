#!/usr/bin/python3
for number in reversed(range(97, 123)):
    if number % 2 == 0:
        pass
    else:
        number = number - 32
    print("{:c}".format(number), end="")
