#!/usr/bin/python3
"""Module defining a Rectangle class inheriting from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    
    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.
        
        Args:
            width (int): The width of the rectangle. Must be a positive integer.
            height (int): The height of the rectangle. Must be a positive integer.
        
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is <= 0.
        """
        # Validate using BaseGeometry's method
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        # Private attributes
        self.__width = width
        self.__height = height
