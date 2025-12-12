#!/usr/bin/python3
"""Check if an object inherits (directly or indirectly) from a class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherits from a_class."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
