#!/usr/bin/python3
""" Cmd Module
"""


import cmd
import re
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Console Interpreter for AirBnB clone
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """If line is empty, do nothing
        """
        return False

    def do_EOF(self, line):
        """Exit the prgram when you get EOF
        """
        return True

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
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = shlex.split(line) # Use shlex to split line
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + '.' + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    if args[2] == "" or args[3] is None:
                        print("** attribute name missing **")
                    else:
                        if not hasattr(storage.all()[key], args[2]):
                            print("** value missing **")
                        else:
                            # Consider another method of casting later
                            # \if this does not work
                            # Cast the value to the original type
                            if re.search('^[+|-]?\d+', args[3]):
                                value = int(args[3])
                            elif re.search('^[+|-]?\d*\.\d*$', args[3]):
                                value = float(args[3])
                            else:
                                value = args[3]
                            # Update the attribute with the new value
                            setattr(storage.all()[key], args[2], value)
                            storage.all()[key].save()
