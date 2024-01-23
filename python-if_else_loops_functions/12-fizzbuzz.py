#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):  # count from 1 to 100

        if i % 3 == 0 and i % 5 == 0:  # if a multiple of 3 and 5
            print("FizzBuzz ", end="")  # print FizzBuzz

        elif i % 3 == 0:  # if i is a multiple of 3 print Fizz
            print("Fizz ", end="")

        elif i % 5 == 0:  # if i is a multiple of 5 print Buzz
            print("Buzz ", end="")

        else:  # if i is not a multiple of 3 or 5 print i
            print(i, " ", end="")
