#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """ finds all multiples of 2 in a list """
    if my_list:
        divisible_items = []
        for item in my_list:
            divisible_items.append(item % 2 == 0)
        return divisible_items
