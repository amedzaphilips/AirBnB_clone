#!/usr/bin/python3
import cmd


class User(cmd.Cmd):
    intro = "The is the interface "
    prompt = "(interface) "
    """This is the cmd module"""

    def do_greet(self, name):
        print("Hello, {}.".format(name))

    def do_exit(self, arg):
        'Exit the command interpreter.'
        print("Goodbye!")
        return True

    def do_EOF(self, arg):
        print("Goodbye there")
        return True

if __name__ == "__main__":
    User().cmdloop()
