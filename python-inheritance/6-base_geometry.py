#!/usr/bin/python3
"""BaseGeometry class with unimplemented area method."""


class BaseGeometry:
    """Represents a base geometry class."""

    def area(self):
        """Raises an exception when area() is called."""
        raise Exception("area() is not implemented")
