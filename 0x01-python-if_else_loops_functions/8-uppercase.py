#!/usr/bin/python3


def uppercase(str):
    for char in str:
        if char in 'abcdefghijklmnopqrstuvwqxyz':
            a = ord(char) - 32
            char = chr(a)
        print("{}".format(char), end="")
    print("")
