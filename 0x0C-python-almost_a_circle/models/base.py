#!/usr/bin/python3
"""Defines a class Base"""
import json
import os.path
import csv
import turtle


class Base:
    """
    Base class for managing id attribute for all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base class.
        Args:
            id (int): instance public attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
