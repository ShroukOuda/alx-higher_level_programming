#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    for n in names:
        if "__" not in n[:2]:
            print("{}".format(n))
