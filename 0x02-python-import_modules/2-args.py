#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args_no = len(argv) - 1
    arg_str = "argument" if args_no == 1 else "arguments"
    print("{} {}{}".format(args_no, arg_str, '.' if args_no == 0 else ':'))
    for i in range(1, args_no + 1):
        print("{}: {}".format(i, argv[i]))
