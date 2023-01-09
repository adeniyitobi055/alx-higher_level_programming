#!/usr/bin/python3
"""
my_list: inherits from list
Return: sorted list in ascending order
"""


class MyList(list):
    """
    MyList: child of list
    """
    def print_sorted(self):
        """
        print_sorted - prints the list, but sorted
        """
        print(sorted(self))
