#!/usr/bin/python3

# Print a basic string :
print("Hello World !")

# Print a string with a variable without casting (using f-string) :
number = 24
print(f"You're {number} years old.")

# Print a float with a variable without casting (using f-string) :
pi = 3.14159
print(f"Pie value is approximately {pi:.2f}")

# Print the concatenation of two strings :
string1 = "Holberton"
string2 = "School"
concatenation = string1 + " " + string2
print(f"Welcome to {concatenation} !")

# Print a different part of a string :
word = "Holberton is a school"
print(f"This is the first 3 letters : {word[:3]}")
print(f"This is the 2 last letters : {word[19:]}")
print(f"This is the middle word : {word[10:-9]}")
