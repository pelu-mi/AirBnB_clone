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
    def __init__(self):
        """
        Initialize the instance of the class with some attributes
        """
        self.id = str(uuid.uuid4())
        now = datetime.now()
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
