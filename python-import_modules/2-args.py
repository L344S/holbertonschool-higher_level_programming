#!/usr/bin/python3

from sys import argv  # import module argv from sys

if len(argv) == 1:  # if no arguments
    print("0 arguments.")  # print there are no arguments
elif len(argv) == 2:  # if 1 argument
    print(f"{len(argv) - 1} argument:")  # print the number of arguments
else:  # if more than 1 argument
    print(f"{len(argv) - 1} arguments:")  # print the number of arguments

for i in range(1, len(argv)):  # for loop through the arguments list
    print(f"{i}: {argv[i]}")  # print the index and the argument
