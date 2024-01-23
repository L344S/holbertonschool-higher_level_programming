#!/usr/bin/python3
from sys import argv  # import module argv from sys
if __name__ == "__main__":
    # initialize args starting from the 2nd argument (1st is the script name)
    args = argv[1:]
    sum = 0  # initialize sum to 0
    for i in args:  # for loop through the arguments list
        sum = sum + int(i)  # add the argument each args[i] to sum
    print(sum)  # print the total sum
