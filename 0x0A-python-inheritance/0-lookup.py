#!/usr/bin/python3
# 0-lookup.py
# Auth: Solomon Nwante
"""Defines object attribute and methods lookup function."""


def lookup(obj):
    """Return a list of object's available attributes and methods."""
    return (dir(obj))
