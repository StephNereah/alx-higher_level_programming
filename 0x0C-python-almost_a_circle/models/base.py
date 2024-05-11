#!/usr/bin/python3

class Base:
    """Class Attributes:
    private class attribute __nb_objects = 0
    class constructor: def __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Args:
        id(int) public class attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = +1
            self.id = Base.__nb_objects
