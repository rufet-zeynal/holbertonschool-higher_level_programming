#!/usr/bin/python3
"""Module: BaseGeometry"""

class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise exception for area()"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
