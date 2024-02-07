#!/usr/bin/python3
'''
deal with arguments and operations
'''
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] == "+":
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print(f"{a} + {b} = {add(a, b)}")
    elif sys.argv[2] == "-":
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print(f"{a} - {b} = {sub(a, b)}")
    elif sys.argv[2] == "*":
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print(f"{a} * {b} = {mul(a, b)}")
    elif sys.argv[2] == "/":
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
