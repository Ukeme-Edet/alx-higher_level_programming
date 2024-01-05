#!/usr/bin/python3
"""
A function that returns a string n times the number of times it has been called
"""


def magic_string():
    """
    Returns a string n times the number of times it has been called
    """
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ", ".join(["Holberton"] * magic_string.count)
