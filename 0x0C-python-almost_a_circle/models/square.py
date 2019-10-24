#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """begin program - python cry"""

    def __init__(self, size, x=0, y=0, id=None):
        """begin program - python cry"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """begin program - python cry"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """begin program - python cry"""
        return self.width

    @size.setter
    def size(self, size):
        """begin program - python cry"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """begin program - python cry"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, attrs[i], e)
            return
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def to_dictionary(self):
        """begin program - python cry"""
        d = {}
        for k, v in vars(self).items():
            if k.startswith("_"):
                if not k.endswith("width") and not k.endswith("height"):
                    idx = k.index("__")
                    d[k[idx + 2:]] = v
                else:
                    d["size"] = v
            else:
                d[k] = v
        return d
