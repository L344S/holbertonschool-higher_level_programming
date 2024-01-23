#!/usr/bin/env python3
def print_last_digit(number):  # Function that prints the last digit of a num
    positive = abs(number)  # abs() returns the absolute (pos) value of a num
    last_digit = positive % 10  # get last digit of + number
    print(last_digit, end="")  # print without new line
    return (last_digit)  # return last digit of number
