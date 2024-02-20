#!/usr/bin/python3
"""Module for Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Description:
            A function to return the JSON string representation
            of list_dictionaries.

        Attributes:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            The JSON string representation of list_dictionaries. (str)
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Description:
            A function to write the JSON string representation
            of list_objs to a file.

        Attributes:
            list_objs (list): A list of instances.

        Calls:
            to_json_string(list_dictionaries) : Calls the static method.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []

        list_dicts = []
        with open(filename, "w") as file:
            for i in list_objs:
                list_dicts.append(i.to_dictionary())
            file.write(Base.to_json_string(list_dicts))
