#!/usr/bin/python3
""" class Mylist defines to inherit from list """


class MyList(list):
    """ the class that inherits from list. """

    def print_sorted(self):
        """Prints the list, but sorted."""
        sorted_list = sorted(self)
        print(sorted_list)
