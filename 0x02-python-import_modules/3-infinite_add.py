#!/usr/bin/python3
from sys import argv
res = 0
for i in range(1, len(argv)):
    res += int(argv[i])
print(res)
