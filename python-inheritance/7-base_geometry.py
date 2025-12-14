#!/usr/bin/python3
"""Module that defines BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with area and integer validation methods"""

    def area(self):
        """Raise an Exception indicating area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
