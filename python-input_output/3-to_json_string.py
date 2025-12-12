#!/usr/bin/python3
""" a string to a text file and returns number of characters added"""

import json

def append_write(filename="", text=""):
    """Appends text to a UTF-8 file and returns number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return json.dumps(my_obj)
