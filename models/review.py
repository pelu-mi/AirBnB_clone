#!/usr/bin/python3
""" Module containing definition for class Review
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review inheriting from BaseModel
    """
    # Class Attributes
    place_id = ""  # Will refer to Place.id
    user_id = ""  # Will refer to User.id
    text = ""
