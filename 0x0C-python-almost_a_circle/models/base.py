#!/usr/bin/python3

class Base:
    """Base class
    Attributes:
        __nb_objects: private class attribure
        id (int): instance public attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor
        Args:
            id (int): instance public attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
