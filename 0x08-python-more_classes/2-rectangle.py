#!/usr/bin/python3

class Rectangle:
    """A Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize class."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
