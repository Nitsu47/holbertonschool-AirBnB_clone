#!/usr/bin/python3
from models.base_model import BaseModel
"""Creates a class named User"""

class User(BaseModel):
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
