#!/usr/bin/python3

from models.base import Base
import json


class Rectangle(Base):
    """begin program - python cry"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """begin program - python cry"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """begin program - python cry"""
        return self.__width

    @property
    def height(self):
        """Gbegin program - python cry"""
        return self.__height

    @property
    def x(self):
        """begin program - python cry"""
        return self.__x

    @property
    def y(self):
        """Gbegin program - python cry"""
        return self.__y

    @width.setter
    def width(self, width):
        """begin program - python cry"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """begin program - python cry"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """begin program - python cry"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """begin program - python cry"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """begin program - python cry"""
        return self.__height * self.__width

    def display(self):
        """begin program - python cry"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """begin program - python cry"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """begin program - python cry"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, attrs[i], e)
            return
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def to_dictionary(self):
        """begin program - python cry"""
        d = {}
        for k, v in vars(self).items():
            d[k.split("__")[-1]] = v
        return d
