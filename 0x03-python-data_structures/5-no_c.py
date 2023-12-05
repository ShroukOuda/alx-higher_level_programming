#!/usr/bin/env python3
def no_c(my_string):
    new_str = ""
    for c in my_string:
        if c.lower() not in ['c']:
            new_str += c
    return new_str
