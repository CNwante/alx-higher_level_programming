#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    ordered_keys = sorted(a_dictionary.keys())
    for key in ordered_keys:
        print('{}: {}'.format(key, a_dictionary[key]))
