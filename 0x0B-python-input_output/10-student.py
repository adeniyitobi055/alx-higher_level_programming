#!/usr/bin/python3
"""
Module class for student (based on 9-student.py)
"""


class Student:
    """
    A class that defines a student by:
    Attributes:
        first_name: name of student
        last_name: name of student
        age: age of student
    Methods:
        __init__ - initializes the student instance
        to_json - retrieves dictionary rep of student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initializes student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            retrieves a dictionary representation of student.
            Args:
                attr (list): attribute names that are to be retrieved.
        """
        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
