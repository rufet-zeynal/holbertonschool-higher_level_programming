#!/usr/bin/python3
"""Module that writes a string to a text file and returns the number of characters"""


def write_file(filename="", text=""):
    """Writes text to a UTF-8 file and returns number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
