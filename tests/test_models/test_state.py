#!/usr/bin/python3
"""
Unittest for State class
"""

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def setUp(self):
        """Set up for the test"""
        self.my_state = State()

    def tearDown(self):
        """Clean up after the test"""
        del self.my_state

    def test_instance_creation(self):
        """Test the creation of a State instance"""
        self.assertIsInstance(self.my_state, State)

    def test_attributes(self):
        """Test the attributes of State class"""
        self.assertTrue(hasattr(self.my_state, 'name'))
        self.assertTrue(hasattr(self.my_state, 'id'))
        self.assertTrue(hasattr(self.my_state, 'created_at'))
        self.assertTrue(hasattr(self.my_state, 'updated_at'))

    def test_types(self):
        """Test the types of State class attributes"""
        self.assertIsInstance(self.my_state.name, str)
        self.assertIsInstance(self.my_state.id, str)
        self.assertIsInstance(self.my_state.created_at, datetime)
        self.assertIsInstance(self.my_state.updated_at, datetime)

    def test_to_dict_method(self):
        """Test the to_dict method of State class"""
        state_dict = self.my_state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(type(state_dict['created_at']), str)
        self.assertEqual(type(state_dict['updated_at']), str)

    def test_str_method(self):
        """Test the __str__ method of State class"""
        string = str(self.my_state)
        self.assertIn("[State]", string)
        self.assertIn("'id':", string)
        self.assertIn("'created_at':", string)
        self.assertIn("'updated_at':", string)


if __name__ == '__main__':
    unittest.main()
