#!/usr/bin/python3
# 1-rectangle.py
# Auth: Solomon Nwante
""" String representation of a rectangle. """


class Rectangle:
    """ Represent a rectangle. """

    def __init__(self, width=0, height=0):
        """ Initailize a new Rectangle.

        Args:
            width (int): The width of the rectangle
            Height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

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
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def draw(self):
        """Return a rectangle represented with # character"""
        chars = ""
        if self.__width == 0 or self.__height == 0:
            return (chars)
        for c in range(self.__height):
            chars += ('#' * self.__width + '\n')
        return (chars[:-1])

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return self.draw()