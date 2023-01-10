#!/usr/bin/python3
"""
5-save_to_json_file module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - writes an object to a text file, using a
    JSON representation
    Args:
        my_obj: string to represent
        filename: name of file
    Return: json representation
    """
    with open(filename, mode="w") as a_file:
        json.dump(my_obj, a_file)
