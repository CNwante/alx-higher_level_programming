#!/usr/bin/python3


def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer"""
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    accumulator = 0
    pre_value = 0

    for i, c in enumerate(roman_string):
        cur_value = roman_dict.get(c, 0)
        if cur_value > pre_value:
            accumulator -= pre_value
        else:
            accumulator += pre_value
        pre_value = cur_value

    accumulator += pre_value
    return accumulator
