#!/usr/bin/python3
def uppercase(str):
    newStr = ""  # initialize newStr to empty string
    for i in str:  # for loop through the string
        ascii = ord(i)  # convert str to ascii value number
        if ascii > 96 and ascii < 123:  # if between 'a' & 'z' means lowercase
            ascii = ascii - 32  # convert to uppercase by subtracting 32
            # convert ascii to char back and add to newStr
            newStr = newStr + chr(ascii)
        else:  # means i is already uppercase character
            newStr = newStr + i  # add i to newStr
    print(newStr)
