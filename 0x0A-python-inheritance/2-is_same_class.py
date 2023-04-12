#!/usr/bin/python3
""" Defines a class checking function """


def is_same_class(obj, a_class):
    """
    Args:
    obj: An object.
    a_class: A class.

    Returns:
    True if the object is exactly an instance of the specified class; otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
