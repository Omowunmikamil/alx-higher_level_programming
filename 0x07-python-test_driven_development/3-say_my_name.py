#!/usr/bin/python3
"""function that prints first name and last name"""


def say_my_name(first_name, last_name=""):
    """Print names
    Args:
        first_name (str): First to print.
        last_name (str): Last to print..
    Raises:
        TypeError: If either; first_name or last_name are not strings.
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
