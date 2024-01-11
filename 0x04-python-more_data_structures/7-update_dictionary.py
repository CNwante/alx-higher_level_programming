#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary"""
    if key not in a_dictionary:
        a_dictionary[key] = value
    for a_key in a_dictionary:
        if a_key == key:
            a_dictionary[a_key] = value
    return a_dictionary
