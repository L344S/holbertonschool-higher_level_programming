#!/usr/bin/python3
if __name__ == "__main__":  # makes sure the code is not executed when imported
    from add_0 import add  # imports add function from add_0 module
    a = 1
    b = 2
    # prints the sum of a and b using add function
    print('{} + {} = {}'.format(a, b, add(a, b)))
