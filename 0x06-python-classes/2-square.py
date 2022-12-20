#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Defines a function named __init__"""
    def __init__(self, size=0):
        """if statement"""
        if type(size) != int:
            """raises an error"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """raises an error"""
            raise ValueError("size must be >= 0")
        else:
            """Initializes __size of self with size"""
            self.__size = size
