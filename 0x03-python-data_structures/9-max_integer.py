#!/usr/bin/python3


def max_integer(my_list=[]):
    """ finds the biggest integer of a list """
    if len(my_list) > 0:
        sorted_list = sorted(my_list)
        return sorted_list[-1]
    return None
