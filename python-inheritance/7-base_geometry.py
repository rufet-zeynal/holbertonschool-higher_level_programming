#!/usr/bin/python3
"""Module: BaseGeometry"""

class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise an exception because area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer"""
        # Reject non-integers AND bools
        if type(value) is not int or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
