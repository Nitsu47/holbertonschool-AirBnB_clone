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
from models import storage


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

    def do_quit(self, args):
        """exits the console"""
        return True

    def do_EOF(self, args):
        """also exits the console"""
        print()
        return True

    def do_help(self, args):
        """shows availables help topics"""
        print(self.h_list)

    def emptyline(self):
        """does nothing when empty lines or spaces"""
        pass

    def do_create(self, args):
        """creates an instance of BaseModel"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.classes_list:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an
        instance based on the class name and id"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.classes_list:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        if f"{arg[0]}.{arg[1]}" not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[f"{arg[0]}.{arg[1]}"])
        return

    def do_destroy(self, args):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.classes_list:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        del storage.all()[f"{arg[0]}.{arg[1]}"]
        storage.save()
        return

    def do_all(self, args):
        """Prints all string representations of instances"""
        arg = args.split()
        if not arg:
            print("** class name missing **")
            return
        if arg[0] not in self.classes_list:
            print("** class doesn't exist **")
            return
        instances = storage.all()
        filtered_instances = [str(instance) for instance in instances.values()
                              if instance.__class__.__name__ == arg[0]]
        print(filtered_instances)

    def do_update(self, args):
        """Updates an instance based on the class name and
        id by adding or updating attribute"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.classes_list:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        if f"{arg[0]}.{arg[1]}" not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[f"{arg[0]}.{arg[1]}"]
        if len(arg) < 3:
            print("** attribute name missing **")
            return
        if len(arg) < 4:
            print("** value missing **")
            return
        setattr(instance, arg[2], arg[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
