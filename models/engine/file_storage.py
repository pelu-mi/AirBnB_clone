#!/usr/bin/python3
"""
Module to define file storage engine
"""


import json
import os
from datetime import datetime


class FileStorage:
    """
    File storage Class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary '__objects'
        """
        return self.__objects

    def new(self, obj):
        """
        Add obj to '__objects' with the key as '<class name>.id'

        Args:
            obj (any): Object to be added into the storage
        """
        # Create the key for the object
        key = obj.__class__.__name__ + '.' + str(obj.id)
        # Add the key to the __objects dictionary
        self.__objects[key] = obj

    def save(self):
        """
        Convert __objects into JSON format and save to __file_path

        Flow of serialization should be
        <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump
        -> <class 'str'> -> FILE
        """
        # Here, we will overwrite the existing file rather than append to it
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            # Create a dict from self.__objects using 'to_dict()' on all objs
            obj_dicts = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(obj_dicts, f)

    def classes(self):
        """ Return a dict containing classes and their constructors
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
        }
        return classes

    def reload(self):
        """
        Deserializes the JSON file to __objects only if the JSON file
        (__file_path) exists. Otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised.
        The Flow of deserialization should be
        FILE -> <class 'str'> -> JSON load -> <class 'dict'>
        -> <class 'BaseModel'>
        """
        # If file does not exist, do nothing
        if not os.path.isfile(self.__file_path):
            return
        # Overwrite '__objects' with content of '__file_path'
        with open(self.__file_path, 'r', encoding='utf-8') as f:
            o = json.load(f)  # We use 'o' so the command can fit on one line
            d = {k: self.classes()[v['__class__']](**v) for k, v in o.items()}
            self.__objects = d

    def attributes(self):
        """ Return a dict of dict containing constructor for attribute values
        """
        attributes = {
            "BaseModel":
                     {
                         "id": str,
                         "created_at": datetime,
                         "updated_at": datetime
                     },
            "User":  {
                         "email": str,
                         "password": str,
                         "first_name": str,
                         "last_name": str
                     },
            "State": {
                         "name": str
                     },
            "City":  {
                         "state_id": str,
                         "name": str
                     },
            "Amenity": {
                         "name": str
                     },
            "Place": {
                         "city_id": str,
                         "user_id": str,
                         "name": str,
                         "description": str,
                         "number_rooms": int,
                         "number_bathrooms": int,
                         "max_guest": int,
                         "price_by_night": int,
                         "latitude": float,
                         "longitude": float,
                         "amenity_ids": list
                     },
            "Review": {
                          "place_id": str,
                          "user_id": str,
                          "text": str
                     }
        }
        return attributes
