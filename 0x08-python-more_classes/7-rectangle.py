#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.height * self.width)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width + self.height) * 2)

    def __str__(self):
        """
        Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        rect = ""
        if self.width != 0 and self.height != 0:
            for i in range(self.height):
                rect += f"{str(self.print_symbol) * self.width}\n"
            rect = rect[:-1]
        return (rect)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1