base_model.py - that defines all common attributes/methods for other classes
console.py - contains the entry point of the command interpreter.
user.py - class User that inherits from BaseModel class with attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
file_storage.py - Holds the FileStorage class that serializes instances to a JSON file and deserializes JSON file to instances.
