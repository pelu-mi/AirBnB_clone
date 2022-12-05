#!/usr/bin/python3
""" Test module for the File_storage module
"""


import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Test case for FileStorage class
    """
    def setUp(self):
        """ Run before every single test
        """
        self.storage = FileStorage()

    def tearDown(self):
        """ Run after every single test
        """
        self.storage._FileStorage__objects = {}
        if os.path.isfile(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_attr(self):
        """ Test Class attributes
        """
        self.assertIsInstance(self.storage._FileStorage__objects, dict)
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_inheritance(self):
        """ Test inheritance from BaseModel
        """
        self.assertIsInstance(self.storage, FileStorage)

    def test_all(self):
        """ Test the all method
        """
        objs = self.storage.all()
        self.assertIsNotNone(objs)
        self.assertEqual(type(objs), dict)
        self.assertIs(objs, self.storage._FileStorage__objects)

    def test_new(self):
        """ Test the new method
        """
        model = BaseModel()
        self.storage.new(model)
        key = model.__class__.__name__ + '.' + str(model.id)
        objs = self.storage.all()
        self.assertIsNotNone(objs[key])

    def test_reload(self):
        """ Test the reload method
        """
        self.storage.reload()
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_save(self):
        """ Test the save method
        """
        model = BaseModel()
        self.storage.new(model)
        key = model.__class__.__name__ + '.' + str(model.id)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(model.to_dict(), self.storage.all()[key].to_dict())


# Run as main file if called
if __name__ == "__main__":
    unittest.main()
