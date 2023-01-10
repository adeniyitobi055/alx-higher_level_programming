#!/usr/bin/python3
"""
Module for class student
"""


class Student:
    """
    class student defines a student by:
    Attributes:
        first_name: name of student.
        last_name: name of student.
        age: age of student.
    Methods:
        __init__ - initializes the student instance
        to_json - retrieves dict rep of student instance
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            retrieves a dictionary representation of student
        """
        return self.__dict__
