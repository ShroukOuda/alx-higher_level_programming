#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 123:
        return True
    else:
        return False


def uppercase(s):
    for c in s:
        print("{:c}"
              .format(ord(c) if not islower(c) else ord(c) - 32),
              end='')
    print("")
