#!/usr/bin/python3
"""Creates class Base Model to inherit for future classes"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """inits id and datetimes for creation and modification"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.now())
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """returns a string with class name, id and dict object"""
        return ("[{}] ({}) {}".format
                (self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the attr updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of  the instance"""
        saved_dict = self.__dict__.copy()
        saved_dict['created_at'] = self.created_at.isoformat()
        saved_dict['updated_at'] = self.updated_at.isoformat()
        saved_dict['__class__'] = self.__class__.__name__
        return saved_dict
