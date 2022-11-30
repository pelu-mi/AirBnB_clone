#!/usr/bin/python3
""" Test module for the Amenity module
"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test case for Amenity class
    """
    def setUp(self):
        """ Run before every single test
        """
        self.model = Amenity()

    def tearDown(self):
        """ Run after every single test
        """
        pass

    def test_attr(self):
        """ Test Class attributes
        """
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, '')

    def test_inheritance(self):
        """ Test inheritance from BaseModel
        """
        self.assertIsInstance(self.model, Amenity)
        self.assertTrue(issubclass(type(self.model), BaseModel))


# Run as main file if called
if __name__ == "__main__":
    unittest.main()
