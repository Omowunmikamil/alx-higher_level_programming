#!/usr/bin/python3
""" Define a class that inherits class checking function """


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of class that inherited from,
       the specified class.
    """
    if isinstance(obj, a_class):
        return True
    return False
