# tests/test_models/test_place.py

from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlace(unittest.TestCase):
    """Test the Place class"""

    def test_instance_creation(self):
        """Test creation of Place instance"""
        my_place = Place()
        self.assertIsInstance(my_place, BaseModel)
        self.assertIsInstance(my_place, Place)
        self.assertEqual(my_place.city_id, "")
        self.assertEqual(my_place.user_id, "")
        self.assertEqual(my_place.name, "")
        self.assertEqual(my_place.description, "")
        self.assertEqual(my_place.number_rooms, 0)
        self.assertEqual(my_place.number_bathrooms, 0)
        self.assertEqual(my_place.max_guest, 0)
        self.assertEqual(my_place.price_by_night, 0)
        self.assertEqual(my_place.latitude, 0)
        self.assertEqual(my_place.longitude, 0)
        self.assertEqual(my_place.amenity_ids, [])

    def test_to_dict_method(self):
        """Test to_dict method of Place class"""
        my_place = Place()
        place_dict = my_place.to_dict()

        # Check if the 'name' key in the dictionary is not equal to '__class__'
        self.assertNotEqual(place_dict.get('name'), '__class__')

    def test_str_method(self):
        """Test __str__ method of Place class"""
        my_place = Place()
        str_representation = str(my_place)

        # Check if the string representation contains the class name and id
        self.assertIn("[Place]", str_representation)
        self.assertIn(str(my_place.id), str_representation)

    def test_update_attributes(self):
        """Test updating attributes of Place instance"""
        my_place = Place()

        # Update attributes
        my_place.city_id = "123"
        my_place.name = "Cozy Apartment"
        my_place.price_by_night = 100

        # Check if the attributes are updated
        self.assertEqual(my_place.city_id, "123")
        self.assertEqual(my_place.name, "Cozy Apartment")
        self.assertEqual(my_place.price_by_night, 100)


if __name__ == "__main__":
    unittest.main()
