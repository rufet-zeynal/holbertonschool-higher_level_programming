#!/usr/bin/python3
"""Student class module"""


class Student:
    """Defines a student with basic info"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the student
        If attrs is a list of strings, only include those attributes
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance
        json is a dictionary with attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
