#!/usr/bin/env python3


def no_c(my_string):
    """Removes all characters 'c' and 'C' from a string."""
    str_list = [char for char in my_string if char not in ['c', 'C']]
    new_str = ''.join(str_list)
    return new_str
