#!/usr/bin/python3
'''--------'''


def write_file(filename="", text=""):
    '''----------'''
    cnt = 0
    with open(filename, "w", encoding="UTF8") as f:
        f.write(text)
    cnt = len(text)
    return cnt
