#!/usr/bin/python3
"""Returns a dictionary of a class instance for JSON serialization"""


def class_to_json(obj):
    """Return obj attributes as a dictionary"""
    return obj.__dict__.copy()
