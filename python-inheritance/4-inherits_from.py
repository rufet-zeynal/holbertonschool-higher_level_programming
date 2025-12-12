#!/usr/bin/python3
""" an object inherits (directly or indirectly) from a class."""


def inherits_from(obj, a_class):
    """ an instance of a class that inherits from a_class."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
