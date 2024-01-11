#!/usr/bin/python3


def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)"""
    uniq_int = set(my_list)
    return sum(uniq_int)
