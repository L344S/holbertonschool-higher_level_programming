#!/usr/bin/python3

# Print a string with a number inside of it
number = 24
print(f"You're {number} years old.")
# or
print(number, "is your age.")

# Get the last digit of a number (positive or negative)
number = 24
last_digit = number % 10  # return last digit of + number
last_digit = -(number % -10)  # return last digit of - number

# Print a suite of elements :
for i in range(0, 10):  # print 0 to 9
    print(i)

for i in range(97, 123):  # print a to z
    i = chr(i)  # convert int to char
    print(i, end='')    # (end='') print without new line

# Print a suite of elements except some :
for i in range(97, 123):  # print a to z
    i = chr(i)  # convert int to char
    if i != 'q' and i != 'e':  # if i (letter) is not 'q' or 'e'
        print(i, end='')    # (end='') print without new line

for i in range(0, 10):  # print 0 to 9
    if i != 4 and i != 6:  # if i is not 4 or 6
        print(i)  # print i without new line

# Print the hexadecimal value of a number :
n = 98
print(hex(n))  # print hexadecimal value of the variable n