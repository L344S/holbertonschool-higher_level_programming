#!/usr/bin/python3
for i in range(97, 123):  # print alphabet
    if i != 101 or i != 113:  # skip 'e' and 'q'
        print(chr(i), end="")  # print each letter from a to z
