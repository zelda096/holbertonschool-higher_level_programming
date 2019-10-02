#!/usr/bin/python3
class Square:
    """Defines an square
    Attributes:
        __size (int): size of square
        __position (int): Gap from edge
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialysing the square
        Args:
            size (int): size of square
        Returns: None
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Take the size
        Args:
            size (int): size of square
        Returns: size
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

    @property
    def position(self):
        """Take the position
        Args:
            size (int): size of square
        Returns: size
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Handle mistakes
        Args:
            position (int): move the square from the margin
        """
        err = "position of tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TyperError(err)
        else:
            if len(value) != 2:
                raise TypeError(err)
            else:
                for i in range(len(value)):
                    if value[i] < 0:
                        raise TypeError(err)
            self.__position = value

    def area(self):
        """ Calculate area of a square
        Args:
            size (int): size of square
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
            for line_empty in range(self.__position[1]):
                print('')
            for row in range(self.__size):
                for col in range(self.__size + self.__position[0]):
                    if col < self.__position[0]:
                        print(' ', end='')
                    else:
                        print('#', end='')
                print('')

