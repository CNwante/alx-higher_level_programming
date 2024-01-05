#!/usr/bin/python3

if __name__ == "__main__":
    """ print number and list of  arguments passed """
    from sys import argv

    total_arg = len(argv) - 1

    if total_arg == 0:
        print("0 arguments.")
    elif total_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(total_arg))
    for i in range(1, total_arg + 1):
        print("{}: {}".format(i, argv[i]))
