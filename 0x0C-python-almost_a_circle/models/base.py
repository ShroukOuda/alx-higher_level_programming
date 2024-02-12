#!/usr/bin/python3
'''------'''
import json


class Base:
    '''-----'''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''-----'''
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''-------'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        '''----'''
        from os import path
        filename = cls.__name__ + ".json"
        if not path.isfile(filename):
            return []
        with open(filename, "r", encoding="utf-8") as file:
            return [cls.create(**d) for d in cls.from_json_string(file.read())]
