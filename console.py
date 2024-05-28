#!/usr/bin/python3
"""This is the file that defines the entry point of the program"""
import cmd


class HBNBCommand(cmd.Cmd):
    """The entry point"""
    prompt = "(hbnb) "

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
