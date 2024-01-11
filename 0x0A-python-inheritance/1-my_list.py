#!/usr/bin/python3
''' list module'''


class MyList(list):
    ''' list class '''
    def print_sorted(self):
        print(sorted(self))
