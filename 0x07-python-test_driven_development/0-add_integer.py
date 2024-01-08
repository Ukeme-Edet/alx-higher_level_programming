#!/usr/bin/python3
"""A module that contains a function that adds 2 integers."""


def add_integer(a, b=98):
    """
    A function that adds 2 integers.
    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.
    Returns:
        The sum of a and b.
    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
