#!/usr/bin/python3
"""
Unittest for Amenity class
"""

from models.base_model import BaseModel
import unittest
from models.amenity import Amenity
from datetime import datetime
from models import storage


class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity class
    """

    def test_instance_creation(self):
        """
        Test creation of Amenity instance
        """
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)
        self.assertIsInstance(my_amenity, BaseModel)
        self.assertTrue(hasattr(my_amenity, 'id'))
        self.assertTrue(hasattr(my_amenity, 'created_at'))
        self.assertTrue(hasattr(my_amenity, 'updated_at'))
        self.assertTrue(hasattr(my_amenity, 'name'))

    def test_attributes_type(self):
        """
        Test attributes types of Amenity instance
        """
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity.id, str)
        self.assertIsInstance(my_amenity.created_at, datetime)
        self.assertIsInstance(my_amenity.updated_at, datetime)
        self.assertIsInstance(my_amenity.name, str)

    def test_save_method(self):
        """
        Test save method of Amenity instance
        """
        my_amenity = Amenity()
        original_updated_at = my_amenity.updated_at
        my_amenity.save()
        self.assertNotEqual(original_updated_at, my_amenity.updated_at)

    def test_to_dict_method(self):
        """
        Test to_dict method of Amenity instance
        """
        my_amenity = Amenity()
        amenity_dict = my_amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['id'], my_amenity.id)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')


if __name__ == '__main__':
    unittest.main()
