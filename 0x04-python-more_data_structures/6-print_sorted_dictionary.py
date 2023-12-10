#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    _dict = sorted(a_dictionary.items())
    for key, value in _dict:
        print(f"{key}: {value}")
