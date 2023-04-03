#!/usr/bin/python3
"""
defines a rectangle with a class
"""


class Rectangle:
    """a representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """intilization of a rectangle"""
        self.height = height
        self.width = width

    def __del__(self):
        """prints a string when instance has been deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        """getter for private instance attribute width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter for private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns a printable string of a rectangle"""
        string = ""
        if self.__width != 0 and self.__height !=0:
            string += "\n".join("#" * self.__width
                                for j in range(self__height))
        return string

    def __repr__(self):
        """returns a string representation of rectangl recreation"""
        return "Rectangl({:d}, {:d}".format(self.__width, self.__height)
