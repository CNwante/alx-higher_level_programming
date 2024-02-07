#!/usr/bin/python3
# 1-my_list.py
# Auth: Solomon Nwante
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        if not all(isinstance(item, type(self[0])) for item in self[1:]):
            raise TypeError("List with mixed types can't be sorted")

        sorted_list = sorted(self)
        print(sorted_list)
