#!/usr/bin/python3
"""
A class Student that defines a student by: (based on 9-student.py)
"""


class Student:
    """
    A class Student that defines a student by: (based on 9-student.py)
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age:
        def __init__(self, first_name, last_name, age):
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
