#!/usr/bin/python3
class Square:
    """Defines an square
    Attributes:
        __size (int): size of square
    """
    def __init__(self, size=0):
        """start the square
        Args:
            size (int): size of square
        Returns: None
        """
        self.size = size

    @property
    def size(self):
        """Take the size
        Args:
            size (int): size of square
        Returns: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Handle mistakes
        Args:
            size (int): size of square
        """

        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Calculate area of a square
        Args:
            size (int): size square
        Returns: area of square
        """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square
        Args:
            size (int): size of square
        """
        if self.__size == 0:
            print('')
        else:
            for row in range(self.__size):
                for col in range(self.__size):
                    print('#', end='')
                print('')
