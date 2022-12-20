#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Define __init__ function"""
    def __init__(self, size=0):
        """if statement"""
        if type(size) != int:
            """raises an error"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """raises an error"""
            raise ValueError("size must be >= 0")
        else:
            """ initialize"""
            self.__size = size
    """Defines area function"""
    def area(self):
        """returns area"""
        self.__size ** 2    
