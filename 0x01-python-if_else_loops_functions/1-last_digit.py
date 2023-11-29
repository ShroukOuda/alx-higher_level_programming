#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = str(number)
if int(string[-1]) > 5:
    print(f"Last digit of {number:d} is {int(string[-1]):d} and is greater than 5")
elif int(string[-1]) == 0:
    print(f"Last digit of {number:d} is {int(string[-1]):d} and is 0")
else:
    print(f"Last digit of {number:d} is {int(string[-1]):d} and is less than 6 and not 0")
