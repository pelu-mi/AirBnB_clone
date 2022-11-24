#!/usr/bin/python3
"""
Module to define file storage engine
"""


import json
import os


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

    def reload(self):
        """
        Deserializes the JSON file to __objects only if the JSON file
        (__file_path) exists. Otherwise, do nothing. 
        If the file doesn’t exist, no exception should be raised

        Flow of deserialization should be
        FILE -> <class 'str'> -> JSON load -> <class 'dict'>
        -> <class 'BaseModel'>
        """
        # Import statement appears in function to avoid circular import
        from models.base_model import BaseModel


        # Use 'classes' to access the constructor for the class
        classes = {
                "BaseModel": BaseModel
        }
        # If file does not exist, do nothing
        if not os.path.isfile(self.__file_path):
            return
        # Overwrite '__objects' with content of '__file_path'
        with open(self.__file_path, 'r', encoding='utf-8') as f:
            obj_dict = json.load(f)
            d = {k: classes[v['__class__']](**v) for k, v in obj_dict.items()}
            self.__objects = d
