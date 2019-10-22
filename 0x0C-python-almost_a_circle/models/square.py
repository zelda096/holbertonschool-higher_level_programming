#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
	def __init__(self, size, x=0, y=0, id=None):
		super().__init__(size, size, x, y, id)

	def __str__(self):
		u = self.id
		m = self.x
		a = self.y
		n = self.width
		h = "[Square]"
		return "{} ({}) {}/{} - {}".format(h, u, m, a, n)

	@property
	def size(self):
		return self.width

	@size.setter
	def size(self, size):
		self.width = size
		self.height = size

	def update(self, *args, **kwargs):
		if args:
			newValue = ["id", "size", "x", "y"]
			for count, elem in enumerate(args):
				setattr(self,newValue[count], elem)
		for key, value in kwargs.items():
				setattr(self, key, value)

	def to_dictionary(self):
		dic = {}
		keyVal = vars(self)
		for k, v in keyVal.items():
			dic[k.split("_Rectangle__")[-1]] = v
		return dic
