#!/usr/bin/python3
""" Test module for the City module
"""


import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ Test case for City class
    """
    def setUp(self):
        """ Run before every single test
        """
        self.model = City()

    def tearDown(self):
        """ Run after every single test
        """
        pass

    def test_attr(self):
        """ Test Class attributes
        """
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "state_id"))
        self.assertEqual(self.model.name, "")
        self.assertEqual(self.model.state_id, "")

    def test_inheritance(self):
        """ Test inheritance from BaseModel
        """
        self.assertIsInstance(self.model, City)
        self.assertTrue(issubclass(type(self.model), BaseModel))

    def test_string(self):
        """ Test values in attributes
        """
        self.model.name = "New Jersey"
        self.model.state_id = "NJ-01"
        self.assertEqual(self.model.name, "New Jersey")
        self.assertEqual(self.model.state_id, "NJ-01")


# Run as main file if called
if __name__ == "__main__":
    unittest.main()
