#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
	def __init__(self, width, height, x=0, y=0, id=None):
		super().__init__(id)
		self.width = width
		self.height = height
		self.x = x
		self.y = y

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, width):
		if not isinstance(width, int):
			raise TypeError("width must be an integer")
		if width <= 0:
			raise ValueError("width must be > 0")
		self._width = width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		if not isinstance(height, int):
			raise TypeError("height must be an integer")
		if height <= 0:
			raise ValueError("height must be > 0")
		self._height = height

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, x):
		if not isinstance(x, int):
			raise TypeError("x must be an integer")
		if x < 0:
			raise ValueError("x must be >= 0")
		self._x = x

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, y):
		if not isinstance(y, int):
			raise TypeError("y must be an integer")
		if y < 0:
			raise ValueError("y must be >= 0")
		self._y = y

	def area(self):
		return self._width * self._height

	def display(self):
		for space1 in range(self._y):
			print()

		for row in range(self._height):
			for space2 in range(self._x):
				print(" ",end="")

			for col in range(self._width):
				print("#", end="")
			print()

	def __str__(self):
		u = self.id
		m = self._x
		a = self._y
		n = self._width
		o = self._height
		h = "[Rectangle]"
		return "{} ({:d}) {:d}/{:d} - {:d}/{:d}".format(h, u, m, a, n, o)

	def update(self, *args, **kwargs):
		if args:
			newValue = ["id", "width", "height", "x", "y"]
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
