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
        self.size = size

   def area(self):
       """calculates the area of a square
        Returns:
            The area of the square
       """
        return (self.__size) ** 2

   @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size
