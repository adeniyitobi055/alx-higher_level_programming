#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """
    read_file: reads a text file (UTF-8) and prints it
    to stdout
    Args:
        filename: name of the file
    """
    with open(filename, "r", encoding="UTF-8") as a_file:
        for line in a_file:
            print(line, end="")
