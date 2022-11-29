#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        number = ord(letter)
        if number >= 97 and number <= 122:
            number = number - 32
        print("{:c}".format(letter), end="")
    print()
