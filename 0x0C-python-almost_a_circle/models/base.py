#!/usr/bin/python3

class Base:
    """ATTRIBUTES:
    private class attribute: __nb_objects = 0
    class constructor: def __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        public instance attribute: id(int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects =+ 1
            self.id = Base.__nb_objects
