#!/usr/bin/env python3
def print_last_digit(number):  # Function that prints the last digit of a num
    if (number >= 0):  # If number is positive
        last = number % 10  # return last digit of + number
    else:  # If number is negative
        last = abs(number) % 10  # return last digit of negative number
    print(last, end="")  # Print last digit
    return last  # Return last digit
