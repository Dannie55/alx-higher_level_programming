#!/usr/bin/python3
"""define a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side sqauare
    """
    def __init__(self, size=0):
        """intializes the square
        Args:
            size (int):size of a side square
        Returns:
             None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculates the area of a square
        Returns:
            The area of the square
        """
        return (self.__size) ** 2
