#!/usr/bin/python3
class Square:
    """Defines an square
    Attributes:
        __size (int): size of square
    """
    def __init__(self, size=0):
        """Making size private
        Args:
            size (int): size of square
        Returns: None
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ Calculate area of square
        Args:
            size (int): size of a side of square
        Returns: area of square
        """
        return self.__size ** 2
