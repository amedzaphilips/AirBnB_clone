#!/usr/bin/python3
"""A file that defines a Parentclass"""
import uuid
from datetime import datetime


class BaseModel:
    """a class BaseModel that defines all common
    attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Instantiatiing with id
        Args:
            string id - assign with an uuid when an instance is created"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """should print:
        [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return a dictionary containing __class__"""
        my_dict = self.__dict__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
