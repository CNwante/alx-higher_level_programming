#!/usr/bin/python3

""" prints the ASCII alphabet, in lowercase, except q and e """

for alphabet in range(97, 123):

    if (alphabet == 101) or (alphabet == 113):
        continue

    print("{}".format(chr(alphabet)), end="")
