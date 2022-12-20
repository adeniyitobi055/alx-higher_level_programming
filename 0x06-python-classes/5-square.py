#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """defines __init__ function"""
    def __init__(self, size=0):
        """initializes __size of self with size"""
        self.__size = size

    @propert
    def size(self):
        """retrieves __size of self"""
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
    """defines area function"""
    def area(self):
        """returns area"""
        return self.__size ** 2
    """defines my print function"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            """range of i"""
            for i in range(self.__size):
                """range of j"""
                for j in range(self.__size):
                    print("#", end="")
                print()
