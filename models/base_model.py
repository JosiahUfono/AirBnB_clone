#!/usr/bin/python3
'''class that defines a common attributes of other classes.'''
from datetime import datetime
from uuid import uuid4

class BaseModel():
	'''Base model class'''

	def __init__(self, *args, **kwargs):
		'''Initialise the base_model class.'''
		self.id = str(uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def to_dict(self):
		object_dictionary = self.__dict__.copy()
		#used to create a copy of a of a class instance

		object_dictionary['__class__'] = self.__dict__.__name__
		#we make thw class name the key

		object_dictionary['created_at'] = self.created_at.isoformat()
		#we are creating the time in isoformat before storgin to json.
		# Best for serialisation
		return object_dictionary

	def __str__(self):
		class_name = self.__class__.__name__
		#to get the instance of the class name and store it as class_name var
		return "[{}] ({}) {}".format(class_name, self.id,  self.__dict__)

user = BaseModel()
