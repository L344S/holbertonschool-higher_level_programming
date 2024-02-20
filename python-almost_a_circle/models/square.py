#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class to define Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Description:
            A function to initialize a Square object.

        Attributes:
            size (int) : The size of the square (width and height).
            x (int)
            y (int)
            id (int) : The id of the object.

        Calls:
            super().__init__(id) : Calls the constructor of Rectangle class.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Description:
            A function to return the string representation of the object.

        Returns:
            The string representation of the object. (str)
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
