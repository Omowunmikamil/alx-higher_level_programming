#!/usr/bin/python3
"""Define a class BaseGeometry with a public instance method"""


class BaseGeometry:
    def area(self):
        """
        Computes the area of the geometry.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
