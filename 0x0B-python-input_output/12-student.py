#!/usr/bin/python3
class Student():

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if attrs is None or type(attrs) is not list:
            return self.__dict__
        json_dict = {}

        for key2 in attrs:
            try:
                if self.__dict__[key2]:
                    json_dict[key2] = self.__dict__[key2]
            except:
                pass

        return json_dict
