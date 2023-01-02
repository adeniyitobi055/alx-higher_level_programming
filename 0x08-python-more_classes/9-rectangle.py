#!/usr/bin/python3
"""Define a class: Rectangle"""


class Rectangle:
    """The rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """returns a rectangle with characters #"""
        if self.__width == 0 or self.__height == 0:
            return ''
        ret = ''
        for i in range(self.__height):
            for j in range(self.__width):
                ret += str(self.print_symbol)
            ret += '\n'
        return ret[:-1]

    def __repr__(self):
        """returns string representation of a rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """del"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates and returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates and returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns biggest rectangle based on its area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
