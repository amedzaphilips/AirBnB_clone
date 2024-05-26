#!/usr/bin/python3
"""File storage Engine"""
import json
from models.base_model import BaseModel


class FileStorage:
    """This is the storage engine
    for serializatione and deserialization"""
    __file_path = "file.json"
    __object = {}

    def all(self):
        """returns the dictionary __object"""
        return self.__object

    def new(self, obj):
        """sets in __objects the obj
        with key <obj class name>.id"""
        self.__object[obj.__class__.__name__ + ".{}".format(obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file
        (path: __file_path)"""
        d_obj = {}
        for key, value in self.__object.items():
            d_obj[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(d_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        filename = self.__file_path
        try:
            with open(filename, "r") as f:
                obj_dict = json.load(f)
                for d in obj_dict.values():
                    oname = d["__class__"]
                    del d["__class__"]
                    self.new(eval(oname)(**d))
        except FileNotFoundError:
            pass
