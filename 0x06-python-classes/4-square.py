#!/usr/bin/python3
'''square module'''


class Square:
    ''' square class '''
    def __init__(self, size=0):
        self.size = size
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        if self.size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        elif self.size < 0:
            raise ValueError("size must be >= 0")
        else:
            return self.size ** 2
