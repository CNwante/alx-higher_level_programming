#!/usr/bin/python3

""" a program that prints numbers from 0 to 99  """

for number in range(0, 100):
    print("{:02}".format(number), end=", ")

    if number == 99:
        print("{}".format(number))
