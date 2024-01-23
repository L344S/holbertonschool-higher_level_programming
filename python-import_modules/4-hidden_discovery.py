#!/usr/bin/python3
# can't test locally hidden_4 contains null bytes + wrong version of python
import hidden_4
if __name__ == "__main__":  # makes sure the code is not executed when imported
    # for loop through the names in hidden_4
    # # dir() returns a list of the names of the functions, variables etc
    for name in dir(hidden_4):
        if ("__" != name[:2]):  # if the name does not start with __
            print(name)  # print the name
