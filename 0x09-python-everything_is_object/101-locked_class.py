#!/usr/bin/python3
"""
   Defines class with no class or object attribute.
   Defining a locked class.
"""


class LockedClass:
    """
    prevent user from creating new Lockedclass attribute dynamically
    unless attribute is called 'first_name'.
    """

    __slots__ = ["first_name"]
