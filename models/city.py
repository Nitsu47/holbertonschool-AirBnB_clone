#!/usr/bin/python3
from models.base_model import BaseModel
"""Creates City Class"""


class City(BaseModel):
    state_id: str = ""  # It will be the state.id
    name: str = ""
