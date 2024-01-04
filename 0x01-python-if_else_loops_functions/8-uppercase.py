#!/usr/bin/python3

""" print a string in uppercase followed by a new line  """


def uppercase(str):
    for char in str:
        if char in 'abcdefghijklmnopqrstuvwqxyz':
            a = ord(char) - 32
            char = chr(a)
        print("{}".format(char), end="")
    print("")
