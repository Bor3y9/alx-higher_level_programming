#!/usr/bin/python3
""" Module For Class Called Rectangle """


class Rectangle:
    """ Represting the rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.

        Args:
            Width (int): The size of the rect.
            Height (int): The height of the rect.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setting the value for the rect width."""
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting the value for the rect height."""
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
