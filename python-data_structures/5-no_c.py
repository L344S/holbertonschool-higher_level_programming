#!/usr/bin/python3
def no_c(my_string):
    neew_string = ""
    for i in my_string:
        if (i != "c" and i != "C"):
            neew_string = neew_string + i
    return neew_string
