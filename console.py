#!/usr/bin/python3
""" Cmd Module
"""


import cmd
import re
import sys
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
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
