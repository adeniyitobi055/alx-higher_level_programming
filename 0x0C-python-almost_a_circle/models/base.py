#!/usr/bin/python3
"""
base module
"""
import json
import os
import csv
import turtle

class Base:
    """
    Base implementation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init - class constructor
        Args:
            id: object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

