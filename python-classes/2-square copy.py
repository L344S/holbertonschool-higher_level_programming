#!/usr/bin/python3
class Square:
    """A class to define a square."""
    def __init__(self, size=0):
        """
        Description:
            Initializes the square with the given parameter size
            and checks if it is not less than 0 or not an integer.

        Args:
            size (int): The size of the square given as an integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
