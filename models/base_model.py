#!/usr/bin/python3
"""
Module documentation for base_model.py
"""


import uuid
from datetime import datetime
from models import storage


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
            storage.new(self)

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
        storage.save()

    def to_dict(self):
        """
        Return dictionary representation of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated"].isoformat()
        
        return dictionary 
