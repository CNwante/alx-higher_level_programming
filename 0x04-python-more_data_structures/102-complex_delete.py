#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary"""
    if value not in a_dictionary.values():
        return a_dictionary

    keys_to_del = []
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_del.append(key)

    for key in keys_to_del:
        a_dictionary.pop(key)
    return a_dictionary
