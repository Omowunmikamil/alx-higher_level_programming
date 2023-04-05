i#!/usr/bin/python3

#This function adds two integers.

def add_integer(a, b=98):
    '''Function that returns a + b

    Args:
        a: should be an int. if not throw error
        b: second int. if not throw error. default val is 98.

        Returns:
        The addition of a + b or a raised TypeError
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not float and type(b) is not int:
        raise TypeError('b must be an integer')

    return int(a + b)
