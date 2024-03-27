#!/usr/bin/python3

""" Module that contains a function that reads from a file """


def read_file(filename=""):
    """reads a file
    """
    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end='')
