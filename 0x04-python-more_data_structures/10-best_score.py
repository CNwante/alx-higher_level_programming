#!/usr/bin/python3

def max_value_by_key(a_dictionary):
    """Returns a key with the biggest integer value"""
    return {key: max(a_dictionary[key]) for key in a_dictionary}
