#!/usr/bin/python3
'''----'''
from models.base import Base


class Rectangle(Base):
    '''---'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_attributes("width", value, False)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_attributes("height", value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_attributes("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_attributes("y", value)
        self.__y = value

    def validate_attributes(self, name, value, eq=True):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0 and eq:
            raise ValueError("{} must be >= 0".format(name))
        if value <= 0 and not eq:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        return self.__width * self.__height

    def display(self):
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for m in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(self.__class__.__name__, self.id,
                   self.x, self.y, self.width, self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
