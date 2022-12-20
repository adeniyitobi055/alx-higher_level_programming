#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """define __init__ function"""
    def __init__(self, size=0):
        """initialize __size of self with size"""
        self.__size = size

    @property
    def size(self):
        """retrieve __size of self"""
        return self.__size

    @size.setter
    def size(self, value):
        """if statement"""
        if type(value) is not int:
            """raise error"""
            raise TypeError("size must be an integer")
        elif value < 0:
            """raise error"""
            raise ValueError("size must be >= 0")
        else:
            """initialize"""
            self.__size = value
    """define area function"""
    def area(self):
        return self.__size ** 2
