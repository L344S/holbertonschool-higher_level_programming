#!/usr/bin/python3
for i in range(0, 100):  # count from 0 to 99
    if i == 99:  # if i is 99
        print(i)  # print i without new line and comma
    else:  # if i is not 99
        print(f"{i:02d}", end=', ')  # print i with 2 digits, comma and space

