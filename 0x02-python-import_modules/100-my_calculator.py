#!/usr/bin/python3

if __name__ == "__main__":
    """
    imports all functions from the file calculator_1.py
    and handles basic operations
    """
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    total_arg = len(argv)
    if total_arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, op, b, ops[op](a, b)))
