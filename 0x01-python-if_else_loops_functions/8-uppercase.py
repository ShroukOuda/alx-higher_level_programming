#!/usr/bin/python3
def uppercase(s):
    for i in range(len(s)):
        if ord(s[i]) > 96 and ord(s[i]) < 123:
            print("{}".format(chr(ord(s[i]) - 32)),
                  end='')
        else:
            print("{}".format(s[i]),
                  end='')
    print("")
