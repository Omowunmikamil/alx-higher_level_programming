#!/usr/bin/python3
"""Define a class BaseGeometry with a public instance method"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """Represents a class Rectangle that inherits from the base class"""
    
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
