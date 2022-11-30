#!/usr/bin/python3
""" Module containing definition for class Place
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """ Class User inheriting from BaseModel
    """
    # Class Attributes
    city_id = ""  # Will refer to City.id
    user_id = ""  # Will refer to User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # Will refer to list of Amenity.id(s)
