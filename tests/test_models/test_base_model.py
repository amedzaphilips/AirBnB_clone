import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test all cases"""

    def test_is_class(self):
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_id(self):
        base = BaseModel()
        base1 = BaseModel()
        self.assertNotEqual(base.id, base1.id)

    def test_update(self):
        base = BaseModel()
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)
    
    def test_str_rep(self):
        base = BaseModel()
        self.assertIsInstance(base, object)

    def test_id_string(self):
        base = BaseModel()
        self.assertIsInstance(base.id, str)
