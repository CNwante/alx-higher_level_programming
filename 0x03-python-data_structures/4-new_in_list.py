#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    replaces an element in a list at a specific position
    without modifying the original list
    """

    if isinstance(my_list, list):
        if idx >= 0 and idx < len(my_list) - 1:
            new_list = my_list.copy()
            new_list[idx] = element
            return new_list
        return my_list
    return None
