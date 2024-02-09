#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        """Test the creation of a BaseModel instance."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel."""
        model = BaseModel()
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_save_method(self):
        """Test the save method of BaseModel."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_attribute_update(self):
        """Test updating attributes of BaseModel."""
        model = BaseModel()
        model.first_name = "John"
        model.save()
        model_dict = model.to_dict()

        self.assertEqual(model.first_name, "John")
        self.assertIn('first_name', model_dict)
        self.assertEqual(model_dict['first_name'], "John")

    def test_reload_method(self):
        """Test reloading a BaseModel instance from a dictionary."""
        model = BaseModel()
        model.first_name = "Betty"
        model.save()

        model_dict = model.to_dict()

        new_model = BaseModel(**model_dict)

        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertEqual(model.updated_at, new_model.updated_at)
        self.assertEqual(model.first_name, new_model.first_name)


if __name__ == '__main__':
    unittest.main()
