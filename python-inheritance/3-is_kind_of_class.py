#!/usr/bin/python3
"""Class instance or subclass"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass, else False"""
    return isinstance(obj, a_class)
