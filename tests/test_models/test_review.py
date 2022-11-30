#!/usr/bin/python3
""" Test module for the Review module
"""


import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ Test case for Review class
    """
    def setUp(self):
        """ Run before every single test
        """
        self.model = Review()

    def tearDown(self):
        """ Run after every single test
        """
        pass

    def test_attr(self):
        """ Test Class attributes
        """
        self.assertTrue(hasattr(self.model, "place_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "text"))
        # Strings
        self.assertEqual(self.model.place_id, '')
        self.assertEqual(self.model.user_id, '')
        self.assertEqual(self.model.text, '')

    def test_inheritance(self):
        """ Test inheritance from BaseModel
        """
        self.assertIsInstance(self.model, Review)
        self.assertTrue(issubclass(type(self.model), BaseModel))


# Run as main file if called
if __name__ == "__main__":
    unittest.main()
