#!/usr/bin/python3
"""
inherits_from module
"""


def inherits_from(obj, a_class):
    """
    inherits_from - checks if an object is an instance of a class
    that inherited(directly or indirectly) from a specified class.
    Args:
        obj: The object to check.
        a_class: The class to match with the object.
    Returns: If the object is an instance of a class - True
    otherwise - False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
