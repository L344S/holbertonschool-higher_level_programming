#!/usr/bin/python3
def uppercase(str):
    for i in str:  # loop through the string one char at a time
        i = ord(i)  # convert str[i] element to ascii value number
        if i > 96 and i < 123:  # if between 'a' & 'z' means lowercase
            i = i - 32  # convert lowercase to uppercase by subtracting 32
            i = chr(i)  # convert ascii value number back to char
        else:  # means i is uppercase character or special character
            i = chr(i)  # convert ascii value number back to char as normal

        print(i, end="")  # print i without new line
    print("")  # print new line between each function call
