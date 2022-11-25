#!/usr/bin/python3
""" Module containing definition for class User
"""


from models.base_model import BaseModel


class User(BaseModel):
    """ Class User inheriting from BaseModel
    """
    # Class Attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""
