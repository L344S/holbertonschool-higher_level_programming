#!/usr/bin/python3
for i in range(0, 100):  # count from 0 to 99
    print(f"{i:02d}", end='')  # print i with 2 digits and no new line
    if i != 99:  # if i is not 99
        print(", ", end='')  # print ", " without new line for all i except 99
