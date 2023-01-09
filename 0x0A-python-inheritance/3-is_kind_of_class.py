#!/usr/bin/python3
"""
is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - checks if an object is an instance,
    or if an inherited instance of a class.
    Args:
        obj: The object to check.
        a_class: The class to match the type of object to.
    Returns: If object is an instance or inherited instance
    of a_class - True, otherwise - False.
    """
    return isinstance(obj, a_class)
