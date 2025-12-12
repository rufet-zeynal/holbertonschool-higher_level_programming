#!/usr/bin/python3
"""Function that appends a string to a text file"""


def append_write(filename="", text=""):
    """Appends text to a UTF-8 text file and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
