#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.engine.file_storage import FileStorage
from shlex import split
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    _classes = {"BaseModel": BaseModel,  "State": State, "City": City,
                "User":User, "Place":Place, "Review":Review, "Amenity":Amenity}

    prompt = "(hbnb) "

    methods = ["all", "show", "count", "update", "destroy", "count"]

    def precmd(self, line):
        """Implement custom commands"""

        if line == '' or not line.endswith(')'):
            return line

        permit = 1

        for clas in self._classes:
            for method in self.methods:
                if line.startswith("{}.{}(".format(clas, method)):
                    permit = 0
        if permit:
            return line

        tmp = ''
        for method in self.methods:
            tmp = line.replace('(', '.').replace(')', '.').split('.')
            if tmp[0] not in self._classes:
                return ' '.join(tmp)
            while tmp[-1] == '':
                tmp.pop()
            if len(tmp) < 2:
                return line
            if len(tmp) == 2:
                tmp = '{} {}'.format(tmp[1], tmp[0])
            else:
                if "," in tmp[2]:
                    sub_tmp = tmp[2].split(",")
                    tmp = "{} {} {} {} {}".format(
                            tmp[1], tmp[0], sub_tmp[0].strip('\"'),
                            sub_tmp[1].replace('"', "").strip(), sub_tmp[2]
                            )
                else:
                    tmp = '{} {} {}'.format(tmp[1], tmp[0], tmp[2].strip('\"'))

            if tmp.startswith(method):
                return tmp

    def do_EOF(self, line):
        """EOF signal to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Handle an empty line (do nothing)
        """
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to the JSON file

        Usage: create <Class name> <param 1> <param 2> <param 3>...
        Param syntax: <key name>=<value>
        """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        parameters = ' '.join(args[1:])

        if class_name not in self._classes:
            print("** class doesn't exit **")
            return

        para_dict = {}

        for item in parameters.split():
            key, value = item.split('=')
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1].replace('_', ' ')

            if '.' in value:
                left, right = value.split('.')
                if left.isdigit() and right.isdigit():
                    para_dict[key] = float(value)
                else:
                    para_dict[key] = value
            elif value.isdigit():
                para_dict[key] = int(value)
            else:
                para_dict[key] = value

        instance = self._classes[class_name](**para_dict)
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Show a string representation of an instance

        Usage: show <class_name> <id>
        """
        if not line:
            print("** class name missing **")
        else:
            try:
                class_name, _id = line.split(" ")
            except ValueError:
                print("** instance id missing **")
            else:
                all_objects = storage.all()
                if class_name in self._classes:
                    instance_key = f"{class_name}.{_id}"
                    if instance_key in all_objects:
                        print(all_objects[instance_key])
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, line):
        """Delete an instance base on the class name and id

        Usage: destroy <class_name> <id>
        """
        if not line:
            print("** class name missing **")
        else:
            try:
                class_name, _id = line.split(" ")
            except ValueError:
                print("** instance id missing **")
            else:
                all_objects = storage.all()
                if class_name not in self._classes:
                    print("** class doesn't exist **")
                else:
                    instance_key = f"{class_name}.{_id}"
                    if instance_key in all_objects:
                        del all_objects[instance_key]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances

        Usage: all [class_name]
        """

        arg = shlex.split(line)
        results = []

        if len(arg) >= 1:
            class_name = arg[0]
            if class_name in self._classes:
                all_objects = storage.all(class_name)
                for key, obj in all_objects.items():
                    #if key.startswith(arg[0]):
                    results.append(str(obj))
                print(results)
            else:
                print("** class doesn't exist **")
        else:
            all_objects = storage.all()
            for obj in all_objects.values():
                results.append(str(obj))
            print(results)

    def do_count(self, line):
        """Prints number of string representsation of all instances

        Usage: count class_name
        """
        all_objects = storage.all()
        count = 0
        arg = split(line)
        if arg[0] in self._classes:
            for key, obj in all_objects.items():
                if key.startswith(arg[0]):
                    count += 1
            print(count)
        else:
            print("** class doesn't exits **")

    def do_update(self, line):
        """Updates an instance based on the class name and id

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split(" ")
        if not args[0]:
            print("** class name missing **")
        else:
            class_name = args[0].strip()
            if class_name in self._classes:
                if len(args) >= 2:
                    _id = args[1].strip()
                    all_object = storage.all()
                    instance_key = f"{class_name}.{_id}"
                    if instance_key in all_object:
                        if len(args) >= 3:
                            attribute_name = args[2].strip()
                            if len(args) >= 4:
                                at_value_str = " ".join(args[3:]).replace(
                                        '"', ""
                                        ).strip()
                                instance = all_object[instance_key]

                                try:
                                    at_value = eval(at_value_str)
                                except (NameError, SyntaxError):
                                    at_value = at_value_str

                                setattr(instance, attribute_name, at_value)
                                instance.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
