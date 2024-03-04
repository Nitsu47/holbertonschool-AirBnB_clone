#!/usr/bin/python3
"""Test for BaseModel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    
    def test_setUp(self):
        # Creates instance for tests.
        base_instance = BaseModel()
        
    def test_base_attr(self):
        # Class exists?.
        self.assertIsInstance(base_instance, BaseModel)

    def test_uuid_verify(self):
        # Checks if creates uuid every time.
        id_1 = BaseModel()
        id_2 = BaseModel()
        self.assertEqual(self.id_1.id, id_2.id)

    def test_str_method(self):
        # Checks if str method works right.
        test_instance = BaseModel()
        str_representation = str(test_instance)
        expected_str = f"[{test_instance.__class__.__name__}]
        ({test_instance.id}) {test_instance.__dict__}"
        self.assertEqual(str_representation, expected_str)

    def test_save(self):
        # Save works right as expected?.
        base = BaseModel()
        saved_updated_at = base.updated_at
        base.save()

        self.assertNotEqual(saved_updated_at, base.updated_at)


    def test_to_dict(self):
        # Dictionary created succesfully?.
        dict_representation = self.base_instance.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertIn('created_at', dict_representation)
        self.assertIn('updated_at', dict_representation)
        self.assertIn('__class__', dict_representation)


if __name__ == '__main__':
    unittest.main()
