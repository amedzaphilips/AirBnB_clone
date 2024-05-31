#!/usr/bin/python3
"""This is the file that defines the entry point of the program"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The entry point"""
    prompt = "(hbnb) "

    def do_create(self, model_name=None):
        """Creates a new instance of BaseModel"""
        base = model_name.split()
        if len(base) == 0:
            print("** class name missing **")
            return
        if base[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        my_model = BaseModel()
        storage.save()
        print(my_model.id)

    def do_show(self, model_name):
        """Prints the string representation of an instance
        based on the class name and id
        Ex: $ show BaseModel 1234-1234-1234"""
        base = model_name.split()
        obj = storage.all()
        if len(base) == 0:
            print("** class name missing **")
            return
        if base[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(base) == 1:
            print("** instance id missing **")
            return
        if "{}.{}".format(base[0], base[1]) not in obj:
            print("** no instance found **")
            return
        print(obj["{}.{}".format(base[0], base[1])])

    def do_destroy(self, model_name):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234"""
        base = model_name.split()
        obj = storage.all()
        if len(base) == 0:
            print("** class name missing **")
            return
        if base[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(base) == 1:
            print("** instance id missing **")
            return
        if "{}.{}".format(base[0], base[1]) not in obj:
            print("** no instance found **")
            return
        del obj["{}.{}".format(base[0], base[1])]
        storage.save()

    def do_all(self, model_name):
        """Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all"""
        base = model_name.split()
        obj = storage.all()
        if len(base) > 0 and base[0] != "BaseModel":
           print("** class doesn't exist **")
           return
        objlist = []
        for name in storage.all().values():
            objlist.append(name.__str__())
        print(objlist)

    def do_update(self, model_name):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"""
        base = model_name.split()
        obj_all = storage.all()
        obj = obj_all["{}.{}".format(base[0], base[1])]
        if len(base) == 0:
            print("** class name missing **")
            return
        if base[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(base) == 1:
            print("** instance id missing **")
            return
        if "{}.{}".format(base[0], base[1]) not in obj_all:
            print("** no instance found **")
            return
        if len(base) == 2:
            print("** attribute name missing **")
            return
        if len(base) == 3:
            print("** value missing **")
            return
        if "{}.{}".format(base[0], base[1]) in obj_all:
            att_name = base[2]
            att_value = base[3].strip('"')
            obj.__dict__[att_name] = att_value
        storage.save()

    def do_EOF(self, line):
        """return True if EOF"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def postloop(self):
        """exit on next line"""
        pass

    def emptyline(self):
        """do nothing and dont't execute the last command"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
