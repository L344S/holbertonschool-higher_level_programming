#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A class to define Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Description:
            A function to initialize a Rectangle object.

        Attributes:
            width (int) : The width of the rectangle.
            height (int) : The height of the rectangle.
            x (int)
            y (int)
            id (int) : The id of the object.

        Calls:
            super().__init__(id) : Calls the constructor of Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Description:
            (G) A function to get the width of the rectangle.

        Returns:
            The width of the rectangle. (int)
        """
        return self.__width

    @property
    def height(self):
        """
        Description:
            (G) A function to get the height of the rectangle.

        Returns:
            The height of the rectangle. (int)
        """
        return self.__height

    @property
    def x(self):
        """
        Description:
            (G) A function to get the x of the rectangle.

        Returns:
            The x (int)
        """
        return self.__x

    @property
    def y(self):
        """
        Description:
            (G) A function to get the y  of the rectangle.

        Returns:
            The y (int)
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Description:
            A function to set the width of the rectangle.

        Args:
            value (int) : The value to set the width to.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Description:
            A function to set the height of the rectangle.

        Args:
            value (int) : The value to set the height to.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """
        Description:
            A function to set the x of the rectangle.

        Args:
            value (int) : The value to set the x to.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """
        Description:
            A function to set the y of the rectangle.

        Args:
            value (int) : The value to set the y to.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = value
