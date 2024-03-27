#!/usr/bin/python3

"""This module returns the list of available
attributes and methods of an object:"""


def lookup(obj):
    """returns all objects in an objects dictionary
        -> as a list
    """
    return dir(obj)
