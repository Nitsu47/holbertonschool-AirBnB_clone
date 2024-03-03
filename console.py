#!/usr/bin/python3
"""Creates the command interpreter with basic cmd commands"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """defines all basic commands of the console"""

    prompt = '(hbnb) '
    classes_list = ["BaseModel", "User", "State", "City",
                    "Amenity", "Place", "Review"]
    int_attr = ["number_rooms", "number_bathrooms", "mac_guest",
                "price_by_night"]
    float_attr = ["latitude", "longitude"]
    h_list = ['Quit - command to exit the programm',
              'EOF - command to exit the program']

    def do_quit(self, *args):
        """exits the console"""
        return True

    def do_EOF(self, *args):
        """also exits the console"""
        print()
        return True

    def do_help(self, *args):
        """shows availables help topics"""
        print(self.h_list)

    def emptyline(self):
        """does nothing when empty lines or spaces"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
