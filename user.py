import cmd


class User(cmd.Cmd):
    """This is the cmd module"""

    def do_greet(self, name):
        print()
