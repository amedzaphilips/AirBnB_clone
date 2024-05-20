#!/usr/bin/python3
"""File storage Engine"""
import json


class FileStorage:
    """This is the storage engine
    for serializatione and deserialization"""
    __file_path = ""
    __object = {}

    def all(self):
        """returns the dictionary __object"""
        return self.__object.__dict__
