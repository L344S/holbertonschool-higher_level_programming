#!/usr/bin/python3
from sys import argv  # import module argv from sys

sum = 0  # initialize sum to 0

for i in range(1, len(argv)):  # for loop through the arguments list
    sum = sum + int(argv[i])  # add the argument each argv[i] to sum

print(sum)  # print the total sum
