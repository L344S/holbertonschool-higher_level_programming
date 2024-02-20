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

    @property
    def size(self):
        """
        Description:
            (G) A function to get the size of the square.

        Returns:
            The size of the square. (int)
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Description:
            A function to set the size of the square.

        Attributes:
            value (int) : The size of the square.

        Calls:
            self.width = value : Calls the setter of width.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Description:
            A function to update the attributes of the object.

        Attributes:
            *args (list) : A list of arguments.
            **kwargs (dict) : A dictionary of arguments.

        Calls:
            super().update(*args, **kwargs) : Calls the update of Rectangle class.
        """
        if args:
            super().update(*args)
        elif kwargs:
            super().update(**kwargs)
