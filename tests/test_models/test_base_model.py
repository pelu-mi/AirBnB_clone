#!/usr/bin/python3
""" Test module for the base_model module
"""


import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """ Test case for User class
    """
    def setUp(self):
        """ Run before every single test
        """
        self.model = BaseModel()

    def tearDown(self):
        """ Run after every single test
        """
        pass

    def test_attr(self):
        """ Test Class attributes
        """
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        # Check Datatype
        model_2 = BaseModel()
        #Check that id is unique
        self.assertNotEqual(self.model.id, model_2.id)
        self.assertEqual(type(self.model.id), str)
        self.assertEqual(type(self.model.created_at), datetime)
        self.assertEqual(type(self.model.updated_at), datetime)

    def test_inheritance(self):
        """ Test inheritance from BaseModel
        """
        self.assertIsInstance(self.model, BaseModel)


# Run as main file if called
if __name__ == "__main__":
    unittest.main()
