#!/usr/bin/python3

"""defines a class Square"""


class square:
    """Represent a square
        Attributes:
    __size (int): size of side
    """
    def __int__(self, size=0):
        """intiialization of sqaure
            Args:
        size (int): size of sides
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
