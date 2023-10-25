#!/usr/bin/python3
"""Square module.
This module contains a class that defines a square with its size.
"""


class Square:
    """represents a square"""
    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
