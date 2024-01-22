#!/usr/bin/python3
for i in range(97, 123):  # print alphabet
    i = chr(i)  # convert ascii int to char (ex : 97 to 'a')
    if i not in 'qe':  # if i is not 'q' or 'e'
        print(i, end='')  # print i without new line
