#!/usr/bin/python3
"""File storage Engine"""
import json


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
        self.__object[self.__class__.__name__ + ".{}".format(obj)] = obj

    def save(self):
        """serializes __objects to the JSON file
        (path: __file_path)"""
        filename = self.__file_path
        with open(filename, "a", encoding="utf-8") as f:
            json.dump(self.__object, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        filename = self.__file_path
        try:
            with open(filename, "r") as f:
                self.__object = json.load(f)
        except FileNotFoundError:
            pass
