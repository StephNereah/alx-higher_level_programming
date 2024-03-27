#!/usr/bin/python3

"""class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle shape, inheirts from basegeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """custom str method for str and print
        """
        string = "[Rectangle] "
        string += str(self.__width) + '/' + str(self.__height)
        return string

    def area(self):
        """overrides parent's method for area for use w/ rectangle
        """
        return (self.__width * self.__height)
