#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):

        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """
        returns area
        """
        return (self.__width * self.__height)

    def __str__(self):

        return ("[{:s}] {:d}/{:d}".
                format(self.__class__.__name__, self.__width, self.__height))
