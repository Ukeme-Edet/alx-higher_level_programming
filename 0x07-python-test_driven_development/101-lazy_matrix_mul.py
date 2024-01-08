#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices using the module
NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies 2 matrices using the module NumPy.
    Args:
        m_a (list): the first matrix
        m_b (list): the second matrix
    Returns:
        list: the result of the multiplication
    Raises:
        TypeError: if m_a or m_b are not lists
        TypeError: if m_a or m_b are not lists of lists
        ValueError: if m_a or m_b are empty lists or matrices
        TypeError: if m_a or m_b contain a non int/float
        TypeError: if m_a or m_b are not rectangular
        ValueError: if m_a or m_b can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(len(row) > 0 for row in m_a) or len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if not all(len(row) > 0 for row in m_b) or len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(n, (int, float)) for row in m_a for n in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(n, (int, float)) for row in m_b for n in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return np.dot(m_a, m_b)
