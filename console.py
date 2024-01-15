#!/usr/bin/python3
'''Console management class'''


import cmd, json
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
	'''Class reponsible for the console app'''
	prompt = "(hbnb)"

	def __init__(self):
		'''Initialised the console'''
		super().__init__()
		self.users = {}

	def do_create(self, hbnb_console):
		'''Method that creates a user'''
		args = hbnb_console.splt()
		if not args:
			print("** class name missing **")

	def do_EOF(self, hbnb_console):
		'''End of file method'''
		print()
		return True

	def do_quit(self, hbnb_console):
		'''Method call to quit the console'''
		return True

if __name__ == '__main__':
	HBNBCommand().cmdloop()
	'''Loop for the console.'''
