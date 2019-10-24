#!/usr/bin/python3

import json
import csv
import os.path


class Base:
    """begin program - python cry"""

    __nb_objects = 0

    def __init__(self, id=None):
        """begin program - python cry."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """begin program - python cry"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list")
        if any(type(x) != dict for x in list_dictionaries):
            raise TypeError("list_dictionaries must contain dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """begin program - python cry"""
        if type(list_objs) != list and list_objs is not None:
            raise TypeError("list_objs must be a list")
        if list_objs is None or list_objs == []:
            output = []
        else:
            first = type(list_objs[0])
            if any(type(x) != first for x in list_objs):
                raise ValueError("all elements of list_objs must match")
            output = [c.to_dictionary() for c in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(output))

    @staticmethod
    def from_json_string(json_string):
        """begin program - python cry"""
        if json_string is None or json_string == "":
            return []
        if type(json_string) != str:
            raise TypeError("json_string must be a string")
        loads = json.loads(json_string)
        for d in loads:
            if type(d) != dict:
                raise ValueError("json_string must contain dictionaries")
        return loads

    @classmethod
    def create(cls, **dictionary):
        """begin program - python cry"""
        test = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        test.update(**dictionary)
        return test

    @classmethod
    def load_from_file(cls):
        """begin program - python cry"""
        filename = str(cls).split(".")[-1][:-2] + ".json"
        if not os.path.exists(filename):
            return []
        res = []
        with open(filename, "r") as f:
            dicts = cls.from_json_string(f.readline())
        for d in dicts:
            res.append(cls.create(**d))
        return res

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """begin program - python cry"""
        if type(list_objs) != list and list_objs is not None \
                or not all(isinstance(x, cls) for x in list_objs):
            raise TypeError("list_objs must be a list")
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                rec_fields = ['id', 'width', 'height', 'x', 'y']
                squ_fields = ['id', 'size', 'x', 'y']
                if cls.__name__ == "Rectangle":
                    writer = csv.DictWriter(f, fieldnames=rec_fields)
                else:
                    writer = csv.DictWriter(f, fieldnames=squ_fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """begin program - python cry"""
        filename = cls.__name__ + ".csv"
        rec_header = ["id", "width", "height", "x", "y"]
        squ_header = ["id", "size", "x", "y"]
        header = rec_header if cls.__name__ == "Rectangle" else squ_header
        res = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                reader = csv.reader(f, delimiter=',')
                for i, row in enumerate(reader):
                    if i > 0:
                        new = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(new, header[j], int(e))
                        res.append(new)
        return res
