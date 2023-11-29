#!/usr/bin/python3
def uppercase(s):
    if s == None:
        return None
    else:
        for i in range(len(s)):
            if ord(s[i]) > 96 and ord(s[i]) < 123:
            print("{}".format(chr(ord(s[i]) - 32)),
                  end='' if i != len(s) - 1 else '\n')
            else:
            print("{}".format(s[i]),
                  end='' if i != len(s) - 1 else '\n')
