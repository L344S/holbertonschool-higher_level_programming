#!/usr/bin/python3
"""A module for a rectangle class."""


class Rectangle:
    """A class to define a rectangle."""

    """Public class attribute."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Description:
            Creates a instance of a rectangle with the given parameters:
            Initializes the width and height and increments the instances nb.
            If no value is given, it defaults to 0.

        Args:
            width (int): The width of the rectangle given as an integer.
            height (int): The height of the rectangle given as an integer.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

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

    def area(self):
        """
        Description:
            Calculates the area (width * height) of the rectangle.

        Returns:
            The area of the rectangle. (int)
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Description:
            Calculates the perimeter (2 * width + 2 * height) of the rectangle.
            If the width or height is 0, it perimeter is 0.

        Returns:
            The perimeter of the rectangle. (int)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Description:
            Returns a string representation of the rectangle
            with the # character.
            If the width or height is 0, it returns an empty string.

        Returns:
            The string representation of the rectangle. (#)
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = ""
            for i in range(self.__height - 1):
                rectangle += str(self.print_symbol) * self.__width + "\n"
            rectangle += str(self.print_symbol) * self.__width
            return rectangle

    def __repr__(self):
        """
        Description:
            Returns a formal string representation of the rectangle.
            EX :  Rectangle(2, 4)

        Returns:
            The formal string representation of the rectangle. (str)
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Description:
            Prints a message when an instance of Rectangle is deleted.
            Decrements the number_of_instances.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
