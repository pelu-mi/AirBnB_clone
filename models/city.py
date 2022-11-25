#!/usr/bin/python3
""" Module containing definition for class City
"""


from models.base_model import BaseModel


class City(BaseModel):
    """ Class City inheriting from BaseModel
    """
    # Class Attributes
    state_id = ""  # Will refer to State.id
    name = ""
