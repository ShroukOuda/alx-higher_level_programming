#!/usr/bin/python3
def uniq_add(my_list=[]):
    sett = set(my_list)
    r = 0
    for i in sett:
        r += i
    return r
