#!/usr/bin/python3

from sys import argv  # import module argv from sys
if __name__ == "__main__":  # makes sure the code is not executed when imported
    # initialize args starting from the 2nd argument (1st is the script name)
    args = argv[1:]
    if (len(args) == 0):  # if no arguments
        print("0 arguments.")
    elif (len(args) == 1):  # if 1 argument
        print("1 argument:")
    else:  # if more than 1 argument
        print(f"{len(args)} arguments:")
    for i in range(len(args)):  # for loop through the arguments list
        print(f"{i + 1}: {args[i]}")  # print the argument index and value
