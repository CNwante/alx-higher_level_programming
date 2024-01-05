#!/usr/bin/python3

if __name__ == "__main__":

    """ prints the result of the addition of all arguments """

    from sys import argv
    args = len(argv)

    sum = 0
    for i in range(1, args):
        sum += int(argv[i])
    print(sum)
