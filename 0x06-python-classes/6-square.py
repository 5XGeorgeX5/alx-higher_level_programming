#!/usr/bin/python3
"""
Define a class square.
"""


class Square:
    """
    A class square the defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initialize a new Square.
        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Access the size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Access the position property
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Return the current square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        prints the square with the character #
        """
        if self.size == 0:
            print()
            return
        print('\n' * self.position[1], end="")
        for i in range(self.size):
            print(' ' * self.position[0], end="")
            print('#' * self.size)
