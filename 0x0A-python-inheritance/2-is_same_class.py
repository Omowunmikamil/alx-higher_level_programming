#!/usr/bin/python3
""" Defines a class checking function """


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of specified class.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
