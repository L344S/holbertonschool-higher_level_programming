#!/usr/bin/python3
"""A module for a square class."""


class Square:
    """A class to define a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Description:
            Creates a instance of a square and
            initializes the size and position attributes with the given param.
            If no value is given, it defaults to 0.

        Args:
            size (int): The size of the square given as an integer.
            position (tuple): The position of the square as a tuple of 2 int.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Description:
            Gets the value of the size attribute and returns it. (getter)

        Returns:
            The value of the size attribute (int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Description:
            Checks the given parameter value and
            sets it to the size attribute. (setter)

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Description:
            Gets the value of the position attribute and returns it. (getter)

        Returns:
            The value of the position attribute (tuple)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Description:
            Checks the given parameter value and
            sets it to the position attribute. (setter)

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Description:
            Calculates the area of the square (size * size) and returns it.

        Returns:
            The area of the square (int)
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Description:
            Prints the square with the character '#' to the STDOUT.

        """
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
