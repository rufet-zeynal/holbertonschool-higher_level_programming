#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """Custom list class with a print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending order without modifying the original."""
        print(sorted(self))
