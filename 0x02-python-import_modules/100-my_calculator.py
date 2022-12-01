#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
    sys.exit(1)


operator = sys.argv[2]

if operator not in ('+', '-', '*', '/'):
    print(f"Unknown operators. Available operators: +, -, * and /")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])

match operator:
    case '+':
        result = add(a, b)
    case '-':
        result = sub(a, b)
    case '*':
        result = mul(a, b)
    case '/':
        result = div(a, b)

if __name__ == '__main__':
    print(f"{a} {operator} {b} = {result}")
