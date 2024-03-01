#!/usr/bin/python3
"""Creates the command interpreter with basic cmd commands"""
import cmd


class HBNBCommand(cmd.Cmd):
    """defines all basic commands of the console"""

    prompt = '(hbnb) '
    h_list = ['Quit - command to exit the programm',
              'EOF - command to exit the program']

    def do_quit(self, *args):
        """exits the console"""
        return True

    def do_EOF(self, *args):
        """also exits the console"""
        return True

    def do_help(self, *args):
        """shows availables help topics"""
        print(self.h_list)

    def emptyline(self):
        """does nothing when empty lines or spaces"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
