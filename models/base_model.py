#!/usr/bin/python3
"""A file that defines a Parentclass"""
import uuid
import datetime


class BaseModel:
    """a class BaseModel that defines all common
    attributes/methods for other classes"""

    def __init__(self):
        """Instantiatiing with id
        Args: 
            string id - assign with an uuid when an instance is created"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()

    def __str__(self):
        """should print:
        [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
