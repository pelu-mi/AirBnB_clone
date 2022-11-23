#!/usr/bin/python3
"""
Module documentation for base_model.py
"""


import uuid
from datetime import datetime


class BaseModel:
    """
    Class Documentation for BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the instance of the class with some attributes
        Takes in *args and **kwargs
        """
        # Loop over kwargs to set attributes based on key, value pairs
        if kwargs is not None and kwargs != {}:
            for key in sorted(kwargs):
                # If the key is '__class__', ignore it
                if key == '__class__':
                    continue
                # Convert date strings into datetime objects for the attribute
                elif key == 'created_at' or key == 'updated_at':
                    time = datetime.strptime(kwargs[key],
                                             '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, time)
                else:
                    setattr(self, key, kwargs[key])
        # Execute this if **kwargs is None or empty dict
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return string representation of object
        """
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at instance attribute
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return dictionary representation of the instance
        """
        dictionary = {x : self.__dict__[x] for x in sorted(self.__dict__)}
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
