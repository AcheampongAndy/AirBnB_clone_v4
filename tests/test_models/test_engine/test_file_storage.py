#!/usr/bin/python3
"""
Unittest for FileStorage class
"""

import unittest
import os
from unittest.mock import patch, mock_open
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up for the test"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after the test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance_creation(self):
        """Test the creation of a FileStorage instance"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_all_method(self):
        """Test the all method of FileStorage class"""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, {})

    def test_new_method(self):
        """Test the new method of FileStorage class"""
        my_model = BaseModel()
        self.storage.new(my_model)
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn("BaseModel." + my_model.id, all_objects)

    @patch('builtins.open', new_callable=mock_open)
    def test_save_method(self, mock_file):
        """Test the save method of FileStorage class"""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        mock_file.assert_called_once_with('file.json', 'w', encoding='utf-8')

    def test_reload_multiple_classes(self):
        """Test the reload method with multiple classes"""
        user = User()
        user_id = user.id
        self.storage.new(user)
        self.storage.save()

        base_model = BaseModel()
        base_model_id = base_model.id
        self.storage.new(base_model)
        self.storage.save()

        self.storage.reload()

        all_objects = self.storage.all()
        self.assertIn("User." + user_id, all_objects)
        self.assertIn("BaseModel." + base_model_id, all_objects)

    def test_get(self):
        """test that get returns an object of a given class by id."""
        storage = models.storage
        obj = State(name='Michigan')
        obj.save()
        self.assertEqual(obj.id, storage.get(State, obj.id).id)
        self.assertEqual(obj.name, storage.get(State, obj.id).name)
        self.assertIsNot(obj, storage.get(State, obj.id + 'op'))
        self.assertIsNone(storage.get(State, obj.id + 'op'))
        self.assertIsNone(storage.get(State, 45))
        self.assertIsNone(storage.get(None, obj.id))
        self.assertIsNone(storage.get(int, obj.id))
        with self.assertRaises(TypeError):
            storage.get(State, obj.id, 'op')
        with self.assertRaises(TypeError):
            storage.get(State)
        with self.assertRaises(TypeError):
            storage.get()

    def test_count(self):
        """test that count returns the number of objects of a given class."""
        storage = models.storage
        self.assertIs(type(storage.count()), int)
        self.assertIs(type(storage.count(None)), int)
        self.assertIs(type(storage.count(int)), int)
        self.assertIs(type(storage.count(State)), int)
        self.assertEqual(storage.count(), storage.count(None))
        State(name='Lagos').save()
        self.assertGreater(storage.count(State), 0)
        self.assertEqual(storage.count(), storage.count(None))
        a = storage.count(State)
        State(name='Enugu').save()
        self.assertGreater(storage.count(State), a)
        Amenity(name='Free WiFi').save()
        self.assertGreater(storage.count(), storage.count(State))
        with self.assertRaises(TypeError):
            storage.count(State, 'op')


if __name__ == '__main__':
    unittest.main()
