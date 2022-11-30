#!/usr/bin/python3
""" Test module for the User module
"""


import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ Test case for User class
    """
    def setUp(self):
        """ Run before every single test
        """
        self.model = User()

    def tearDown(self):
        """ Run after every single test
        """
        pass

    def test_attr(self):
        """ Test Class attributes
        """
        self.assertTrue(hasattr(self.model, "email"))
        self.assertTrue(hasattr(self.model, "password"))
        self.assertTrue(hasattr(self.model, "first_name"))
        self.assertTrue(hasattr(self.model, "last_name"))
        # Strings
        self.assertEqual(self.model.email, '')
        self.assertEqual(self.model.password, '')
        self.assertEqual(self.model.first_name, '')
        self.assertEqual(self.model.last_name, '')

    def test_inheritance(self):
        """ Test inheritance from BaseModel
        """
        self.assertIsInstance(self.model, User)
        self.assertTrue(issubclass(type(self.model), BaseModel))


# Run as main file if called
if __name__ == "__main__":
    unittest.main()
