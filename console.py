#!/usr/bin/python3
'''Console mangement class'''

import cmd, json
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
	prompt = "(hbnb)"

	def __init__(self):
		super().__init__()
		self.users = {}

	def do_create(self, hbnb_console):
		args = hbnb_console.splt()
		if not args:
			print("** class name missing **")

	def do_EOF(self, hbnb_console):
		print()
		return True

	def do_quit(self, hbnb_console):
		return True

if __name__ == '__main__':
	HBNBCommand().cmdloop()
