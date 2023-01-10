#!/usr/bin/python3
"""
2-append_write module
"""


def append_write(filename="", text=""):
    """
    append_write - appends a string at the end of a text file (UTF-8)
    and returns the number of characters added
    Args:
        filename: name of the file
        text: characters added
    Return: number of bytes written
    """
    with open(filename, mode="a", encoding="UTF-8") as a_file:
        return (a_file.write(text))
