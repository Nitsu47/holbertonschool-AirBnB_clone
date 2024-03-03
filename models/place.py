#!/usr/bin/python3
from models.base_model import BaseModel
"""Creates Place class"""


class Place(BaseModel):
    city_id: str = ""  # It will be the City.id
    user_id: str = ""  # It will be the User.id
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids = []  # It will be the list of the Amenity.id later
