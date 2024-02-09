# tests/test_models/test_user.py

import unittest
from models.user import User
from datetime import datetime
from models import storage


class TestUser(unittest.TestCase):
    """
    Test the User class
    """

    def setUp(self):
        """
        Set up for the test
        """
        self.my_user = User()
        self.my_user.email = "test@example.com"
        self.my_user.password = "password123"
        self.my_user.first_name = "John"
        self.my_user.last_name = "Doe"
        storage.new(self.my_user)
        storage.save()

    def tearDown(self):
        """
        Tear down for the test
        """
        storage.save()

    def test_attributes(self):
        """
        Test the attributes of User class
        """
        self.assertEqual(self.my_user.email, "test@example.com")
        self.assertEqual(self.my_user.password, "password123")
        self.assertEqual(self.my_user.first_name, "John")
        self.assertEqual(self.my_user.last_name, "Doe")

    def test_to_dict(self):
        """
        Test the to_dict method of User class
        """
        user_dict = self.my_user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password123")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")

    def test_created_at(self):
        """
        Test the created_at attribute of User class
        """
        self.assertIsInstance(self.my_user.created_at, datetime)

    def test_updated_at(self):
        """
        Test the updated_at attribute of User class
        """
        self.assertIsInstance(self.my_user.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
