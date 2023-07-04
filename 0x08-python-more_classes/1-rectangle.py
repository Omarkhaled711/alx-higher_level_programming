#!/usr/bin/python3
""" A part of alx tasks on oop """


class Rectangle:
    """ A rectangle class """
    def __init__(self, width=0, height=0):
        """ an initializer for any object of type Rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for the width attribute """
        return self.__width

    @width.setter
    def width(self, width):
        """ setter for the width attribute """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("widht must be >= 0")
        self.__width = width

    @property
    def height(self):
        """ getter for the height attribute """
        return self.__height

    @height.setter
    def height(self, height):
        """ setter for the height attribute """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
