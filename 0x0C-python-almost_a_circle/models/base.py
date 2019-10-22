#!/usr/bin/python3
import json
class Base:
	_objects = 0

	def __init__(self, id=None):
		if id is not None:
			self.id = id
		else:
			Base._objects += 1
			self.id = Base._objects

	@staticmethod
	def to_json_string(list_dictionaries):
		if not isinstance(list_dictionaries, list):
			raise TypeError("list_dictionaries must be a list")
		elif list_dictionaries is None or list_dictionaries == []:
			return "[]"
		else:
			return json.dumps(list_dictionaries)

	@classmethod
	def save_to_file(cls, list_objs):
		if not isinstance(list_objs, list):
			raise TypeError("list_objs must be a list")
		if list_objs is None or list_objs == []:
			emptyList = []
		else:
			output = [c.to_dictionary() for c in list_objs]
			file = cls.__name__ + ".json"
			with open(file, mode='w', encoding='utf-8') as myFile:
				myFile.write(cls.to_json_string(output))

	@staticmethod
	def from_json_string(json_string):
		if not isinstance(json_string, str):
			raise TypeError("json_string must be a string")
		if json_string is None or json_string == "":
			output = []
			return output
		else:
			return json.loads(json_string)

	@classmethod
	def create(cls, **dictionary):
		if cls.__name__ == "Rectangle":
			a = cls(2, 4, 6, 8, 10)
			a.update(**dictionary)
			return a
		if cls.__name__ == "Square":
			a = cls(2, 2, 6, 8, 10)
			a.update(**dictionary)
			return a
