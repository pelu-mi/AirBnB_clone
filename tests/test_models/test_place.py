#!/usr/bin/python3
""" Test module for the Amenity module
"""


import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test case for Amenity class
    """
    def setUp(self):
        """ Run before every single test
        """
        self.model = Place()

    def tearDown(self):
        """ Run after every single test
        """
        pass

    def test_attr(self):
        """ Test Class attributes
        """
        self.assertTrue(hasattr(self.model, "city_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "description"))
        self.assertTrue(hasattr(self.model, "number_rooms"))
        self.assertTrue(hasattr(self.model, "number_bathrooms"))
        self.assertTrue(hasattr(self.model, "max_guest"))
        self.assertTrue(hasattr(self.model, "price_by_night"))
        self.assertTrue(hasattr(self.model, "latitude"))
        self.assertTrue(hasattr(self.model, "longitude"))
        self.assertTrue(hasattr(self.model, "amenity_ids"))
        # Strings
        self.assertEqual(self.model.city_id, '')
        self.assertEqual(self.model.user_id, '')
        self.assertEqual(self.model.name, '')
        self.assertEqual(self.model.description, '')
        # Integers
        self.assertEqual(self.model.number_rooms, 0)
        self.assertEqual(self.model.number_bathrooms, 0)
        self.assertEqual(self.model.max_guest, 0)
        self.assertEqual(self.model.price_by_night, 0)
        # Floats
        self.assertEqual(self.model.latitude, 0.0)
        self.assertEqual(self.model.longitude, 0.0)
        # List
        self.assertEqual(self.model.amenity_ids, [])

    def test_inheritance(self):
        """ Test inheritance from BaseModel
        """
        self.assertIsInstance(self.model, Place)
        self.assertTrue(issubclass(type(self.model), BaseModel))


# Run as main file if called
if __name__ == "__main__":
    unittest.main()
