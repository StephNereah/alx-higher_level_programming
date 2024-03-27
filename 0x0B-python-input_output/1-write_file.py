#!/usr/bin/python3

""" Module that contains a function that returns the number of lines
    of a text file
"""


def number_of_lines(filename=""):
    """gets the number of lines from filename
    """
    with open(filename, encoding='utf-8') as myFile:
        return sum([1 for line in myFile])
