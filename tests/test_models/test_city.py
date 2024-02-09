# tests/test_models/test_city.py

from models.city import City
from models.base_model import BaseModel
import unittest


class TestCity(unittest.TestCase):
    """Test the City class"""

    def test_instance_creation(self):
        """Test creation of City instance"""
        my_city = City()
        self.assertIsInstance(my_city, BaseModel)
        self.assertIsInstance(my_city, City)
        self.assertEqual(my_city.state_id, "")
        self.assertEqual(my_city.name, "")

    def test_to_dict_method(self):
        """Test to_dict method of City class"""
        my_city = City()
        city_dict = my_city.to_dict()

        # Check if the 'name' key in the dictionary is not equal to '__class__'
        self.assertNotEqual(city_dict.get('name'), '__class__')

    def test_str_method(self):
        """Test __str__ method of City class"""
        my_city = City()
        str_representation = str(my_city)

        # Check if the string representation contains the class name and id
        self.assertIn("[City]", str_representation)
        self.assertIn(str(my_city.id), str_representation)

    def test_update_attributes(self):
        """Test updating attributes of City instance"""
        my_city = City()

        # Update attributes
        my_city.state_id = "CA"
        my_city.name = "San Francisco"

        # Check if the attributes are updated
        self.assertEqual(my_city.state_id, "CA")
        self.assertEqual(my_city.name, "San Francisco")


if __name__ == "__main__":
    unittest.main()
