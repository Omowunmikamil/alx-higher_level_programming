#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
            Args:
                size (int): The size of the new square.
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Computes the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """print representation of the square."""
        return (f"[Square] {self.__size}/{self.__size}")
