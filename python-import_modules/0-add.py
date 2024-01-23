#!/usr/bin/python3
from add_0 import add  # imports add function from add_0 module
if __name__ == "__main__":  # makes sure the code is not executed when imported
    a = 1
    b = 2
    print(f"{a} + {b} = {add(a, b)}")  # prints the sum of a and b
