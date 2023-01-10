#!/usr/bin/python3
"""
6-load_from_json_file module
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file - creates an object from a 'JSON file'
    Args:
        filename: name of the file
    """
    with open(filename, mode="r") as a_file:
        my_obj = json.load(a_file)
        return my_obj
