#!/usr/bin/python3
"""Module that defines BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with area and integer validation methods"""

    def area(self):
        """Raise an Exception indicating area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is a positive integer.

        Args:
            name (str): name of the parameter
            value: value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
