#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """ print all integers of a list """
    if not my_list:
        return (None)

    for item in range(len(my_list)):
        print("{:d}".format(my_list[item]))
