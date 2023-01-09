#!/usr/bin/python3
"""
is_same_class module
"""


def is_same_class(obj, a_class):
    """
    is_same_class - checks if an object is exactly an instance of
    a given class.
    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns: If object is exactly an instance of a_class - True,
    otherwise - False.
    """
    return True if type(obj) is a_class else False
