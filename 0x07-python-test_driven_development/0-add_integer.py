#!/usr/bin/python3
"""
This module defines a function (`add_integer`) that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers.
    Args:
        a (int): first integer.
        b (int): second integer.
    Returns:
        The addition of the two integers.
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
