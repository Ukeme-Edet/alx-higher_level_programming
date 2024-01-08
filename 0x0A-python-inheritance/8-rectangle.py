#!/usr/bin/python3
"""
A module that contains the Rectangle class inheriting from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializer function that validates the values of width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
