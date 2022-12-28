#!/usr/bin/python3
"""
Module add_integer
a and b arguments
return sum of a and b
"""
def add_integer(a, b=98):
    """
    add_integer
    """
    if type(a) is not int and type(a) is not float:
        raise ValueError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise ValueError("b must be an integer")
    return (int(a) + int(b))
