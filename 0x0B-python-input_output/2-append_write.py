#!/usr/bin/python3
'''---------'''


def append_write(filename="", text=""):
    '''--------'''
    cnt = 0
    with open(filename, 'a', encoding='UTF8') as f:
        f.write(text)
    cnt = len(text)
    return cnt
