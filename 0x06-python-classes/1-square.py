#!/usr/bin/python3
class Square:
    """Defines an square
    Attributes:
        __size (int): size of square
    """
    def __init__(self, size):
        """Making size private
        Args:
            size (int): size of square
        Returns: None
        """
        self.__size = size
