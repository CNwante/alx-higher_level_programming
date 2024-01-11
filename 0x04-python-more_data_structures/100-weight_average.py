#!/usr/bin/python3


def weight_average(my_list=[]):
    """Rreturns the weighted average of all integers tuple"""
    if not my_list:
        return 0

    weight = 0
    size = 0

    for tupl in my_list:
        weight += tupl[0] * tupl[1]
        size += tupl[1]
    average = weight / size
    return average
