#!/usr/bin/python3
from models.base_model import BaseModel
"""Creates the Review Class"""


class Review(BaseModel):
    place_id: str = ""  # It will be the Place.id
    user_id: str = ""  # It will be the User.id
    text: str = ""
