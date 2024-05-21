#!/usr/bin/env python3
""" This is a test file for the BaseModel """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test all cases"""

    def test_is_class(self):
        """ Test if instance created is object of class """
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_id(self):
        """ Test if id's are unique """
        base = BaseModel()
        base1 = BaseModel()
        self.assertNotEqual(base.id, base1.id)

    def test_update(self):
        """ Test if updated time and created times are unique """
        base = BaseModel()
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)

    def test_str_rep(self):
        """ Test if base inherits from object """
        base = BaseModel()
        self.assertIsInstance(base, object)

    def test_id_string(self):
        """ Test if base is a string """
        base = BaseModel()
        self.assertIsInstance(base.id, str)

    def test_dict(self):
        """Test to_dict method"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)

    def test_str(self):
        base = BaseModel()
        self.assertTrue(str(base))

    def test_datetime(self):
        """test the current date time"""
        base = BaseModel()
        self.assertEqual(datetime, type(base.created_at))
        self.assertEqual(datetime, type(base.updated_at))
        
    def test_no_arg_to_BaseModel(self):
        """test if no args"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_save(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.save(None)
