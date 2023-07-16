#!/usr/bin/python3
"""
The console the entry point of the
command interpreter
"""

from models.user import User
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import models
import cmd
import re
import shlex


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand for commands creation
    """
    # Prompt to be displayed
    prompt = '(hbnb) '
    # Using a list to store the base class and all other classes
    class_list = ['BaseModel', 'User', 'State',
                  'City', 'Amenity', 'Place', 'Review']

    def do_EOF(self, args):
        """
        Exits the program
        """
        return True

    def do_quit(self, args):
        """
        Exit the program
        """
        return True

    def do_create(self, line):
        """
        Creates and stores objects
        """
        args = line.split()
        if not self.verify_class(args):
            return
        inst = eval(str(args[0]) + '()')
        if not isinstance(inst, BaseModel):
            return
        inst.save()
        print(inst.id)

    def do_show(self, line):
        """
        Prints a string representation of an instance
        """
        args = line.split()
        # If not verify return
        if not self.verify_class(args):
            return
        if not self.verify_id(args):
            return
        string_key = str(args[0]) + '.' + str(args[1])
        objects = models.storage.all()
        print(objects[string_key])

    def do_destroy(self, line):
        """
        Delete an instance
        """
        args = line.split()
        if not self.verify_class(args):
            return
        if not self.verify_id(args):
            return
        string_key = str(args[0]) + '.' + str(args[1])
        objects = models.storage.all()
        models.storage.delete(objects[string_key])
        models.storage.save()

    def do_all(self, line):
        """
        Should print the list of strings of all instances
        regardless of class
        """
        args = line.split()
        objects = models.storage.all()
        print_list = []
        if len(args) == 0:
            # Should print classes
            for value in objects.values():
                print_list.append(str(value))
        elif args[0] in self.class_list:
            # Should only print arg[0] class instances
            for (key, value) in objects.items():
                if args[0] in key:
                    print_list.append(str(value))
        else:
            print("** class doesn't exist **")
            return False
        print(print_list)

    def do_update(self, line):
        """
        Update the instance based on cls (name)
        and
        id by adding or updating attr
        """
        args = shlex.split(line)
        if not self.verify_class(args):
            return
        if not self.verify_id(args):
            return
        if not self.verify_attribute(args):
            return
        string_key = str(args[0]) + '.' + str(args[1])
        objects = models.storage.all()
        my_dict = objects[string_key].to_dict()
        attr_name = args[2]
        attr_value = args[3]
        for (key, value) in my_dict.items():
            try:
                if attr_name in key:
                    obj_dir = objects[string_key].__dir__()
                    if key in obj_dir:
                        val_c_attr = obj_dir[obj_dir.index(key)]
                        obj = eval('objects[string_key].__class__.' +
                                   val_c_attr)
                        if type(obj) is list:
                            print('converting list')
                            attr_value = eval(attr_value,
                                              {'__builtins__': None},
                                              {})
                        else:
                            attr_value = obj.__class__(attr_value)
            except KeyError:
                return
        setattr(objects[string_key], attr_name, attr_value)
        objects[string_key].save()

    def default(self, line):
        """
        If input is not recognized call this method
        """
        full_list = []
        args = line.split(".")
        if len(args) < 2:
            print('provide more than one argument please')
            return
        cl_name = args[0]
        action = args[1].rstrip('()').lower()
        all_objs = models.storage.all()
        for (key, value) in all_objs.items():
            two_keys = key.split(".")
            if cl_name == two_keys[0]:
                full_list.append(value)
        if 'all' in action:
            print([str(val) for val in full_list])
        elif 'count' in action:
            print(len(full_list))
        elif 'show' in action:
            try:
                c_id = args[1][6:-2]
                print(all_objs[cl_name + '.' + c_id])
            except Exception as e:
                print('** no instance found **')
        elif 'destroy' in action:
            try:
                c_id = args[1][9:-2]
                models.storage.delete(all_objs[cl_name + '.' + c_id])
            except Exception as e:
                print('** no instance found **')
        elif 'update' in action:
            pass
        else:
            print(action)
            print('** default method not found **')

    @classmethod
    def verify_class(cls, args):
        """
        Class verification
        """
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in cls.class_list:
            print("** class doesn't exist **")
            return False
        return True

    @staticmethod
    def verify_id(args):
        """
        ID verification
        """
        if len(args) < 2:
            print("** instance id missing **")
            return False
        objects = models.storage.all()
        string_key = str(args[0]) + '.' + str(args[1])
        if string_key not in objects.keys():
            print("** no instance found **")
            return False
        return True

    @staticmethod
    def verify_attribute(args):
        """
        Attribute verification
        """
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        return True

    def emptyline(self):
        """
        If no argument no execution
        """
        pass

    def postloop(self):
        """
        Stop after reaching the loop
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
