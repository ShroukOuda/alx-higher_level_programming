#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is  None:
        return None
    Max = 0
    for i in my_list:
        if Max < i:
            Max = i
    return Max
