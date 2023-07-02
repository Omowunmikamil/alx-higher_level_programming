#!/usr/bin/python3
"""Find peak in list of unsorted integers
"""


def find_peak(list_of_integers):
    """Find peak in unsorted integers
    """
    length = len(list_of_integers)

    if length == 0:
        return None
    elif length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    list_of_integers.sort(reverse=True)

    return list_of_integers[0]
