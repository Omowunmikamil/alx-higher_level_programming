#!/usr/bin/python3
""" function that lookup an object attribute """


def lookup(obj):
    """
    returns the list of available attributes
    """
    return dir(obj)
