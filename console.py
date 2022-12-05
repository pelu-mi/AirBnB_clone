#!/usr/bin/python3
""" Cmd Module
"""


import cmd
import re
import sys
import json
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Console Interpreter for AirBnB clone
    """
    prompt = "(hbnb) "

    # Default methods
    def precmd(self, line):
        """Precmd override
        """
        regex = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not regex:
            return line
        class_name = regex.group(1)
        command = regex.group(2)
        args = regex.group(3)
        # Check for the arguments in args
        regex_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if not regex_args:
            user_id = args
            attributes = None
        else:
            user_id = regex_args.group(1)
            attributes = regex_args.group(2)

        values = ""
        if command == "update" and attributes is not None:
            # Specially handle update with dictionary
            regex_dictionary = re.search('^({.*})$', attributes)
            if regex_dictionary:
                self.update_dictionary(class_name, user_id, match_dict.group(1))
                return ""
            # Organize all the values into a string: regex_values as re_vals
            re_vals = re.search('^(?:"([^"]*)")?(?:, (.*))?$', attributes)
            if re_vals:
                # Using v instead of values for pycodestyle sake
                v = (re_vals.group(1) or "") + " " + (re_vals.group(2) or "")
                values = v
        # Recreate string to run as command
        command = command + " " + class_name + " " + user_id + " " + values
        return command

    def emptyline(self):
        """If line is empty, do nothing
        """
        return False

    def do_EOF(self, line):
        """Exit the prgram when you get EOF
        """
        return True

    # hbnb Commands
    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_create(self, line):
        """Create an instance of a class, save it to JSON file
        and print the id.
        ------------------------------------------------------
        Example: $ create BaseModel
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            # Create a new object based on the class called with create
            new_obj = storage.classes()[line]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        classname and id
        ---------------------------------------------------------------
        Example: $ show BaseModel 1234-1234-1234
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + '.' + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Delete an instance based on the class name and id
        and save the changes into the JSON file.
        ----------------------------------------------------
        Example: $ destroy BaseModel 1234-1234-1234
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + '.' + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Print all string representation of all instances based on the
        class name if provided
        ----------------------------------------------------------------
        Example: $ all BaseModel
                 $ all
        """
        if line == "" or line is None:
            output = [str(obj) for key, obj in storage.all().items()]
            print(output)
        else:
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                output = [str(obj) for key, obj in storage.all().items()
                          if type(obj).__name__ == args[0]]
                print(output)

    def do_update(self, line):
        """Update an instance based on the class name and id by adding
        or updating the attribute and save the change to the JSON file).
        ----------------------------------------------------------------
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = tuple(shlex.split(line))
        objects = storage.all()
        if not args:
            print("** class name missing **")
            return 0
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
            return 0
        elif len(args) < 2:
            print("** instance id missing **")
            return 0
        elif len(args) < 3:
            print("** attribute name missing **")
            return 0
        elif len(args) < 4:
            print("** value missing **")
            return 0

        key = "{}.{}".format(args[0], args[1])
        try:
            objects[key].__dict__[args[2]] = args[3]
            storage.save()
        except Exception:
            print("** no instance found **")
            return

    def do_count(self, line):
        """Count the number of instances of a class
        -------------------------------------------
        Usage: <class name>.count()
        Example: User.count()
        """
        args = line.split(' ')
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            id_match = args[0] + '.'
            regex_class = [i for i in storage.all() if i.startswith(id_match)]
            print(len(regex_class))

    # Method to run if dictionary is passed into update method
    def update_dictionary(self, class_name, user_id, dictionary):
        """ Run this command if dictionary is passed into update method
        """
        temp = dictionary.replace("'", '"')
        obj_dict = json.loads(temp)
        if not class_name:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif user_id is None:
            print("** instance id missing **")
        else:
            key = class_name + '.' + user_id
            if key not in storage.all():
                print("** no instance found **")
            else:
                for key, value in obj_dict.items():
                    self.do_update(user_id + ' ' + class_name + ' ' + key + ' ' + value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
