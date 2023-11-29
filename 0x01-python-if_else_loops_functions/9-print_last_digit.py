#!/usr/bin/python3
def print_last_digit(number):
    string = str(number)
    num = int(string[-1])
    print("{}".format(num), end='')
    return (num)
