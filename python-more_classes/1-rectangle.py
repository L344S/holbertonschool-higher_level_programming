#!/usr/bin/python3
"""A module for a rectangle class."""


class Rectangle:
    """A class to define a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Description:
            Creates a instance of a rectangle and
            initializes the width and height attributes with the given param.
            If no value is given, it defaults to 0.

        Args:
            width (int): The width of the rectangle given as an integer.
            height (int): The height of the rectangle given as an integer.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        Description:
            Gets the value of the height attribute and returns it. (getter)

        Returns:
            The value of the height attribute (int)
        """
        return self.__height

    @property
    def width(self):
        """
        Description:
            Gets the value of the width attribute and returns it. (getter)

        Returns:
        The value of the width attribute (int)
        """
        return self.__width

    @height.setter
    def height(self, value):
        """
        Description:
            Checks the given parameter value and
            sets it to the height attribute. (setter)

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        """
        Description:
            Checks the given parameter value and
            sets it to the width attribute. (setter)

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
