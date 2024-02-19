#!/usr/bin/python3
"""Module for Base class"""


class Base:
    """A class to define Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Description:
            A function to initialize a Base object.
        
        Attributes:
            id (int): The id of the object.
            if id is not None, the id is set with this integer.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects