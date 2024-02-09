#!/usr/bin/python3
"""
Unittest for Review class
"""

import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def setUp(self):
        """Set up for the test"""
        self.my_review = Review()

    def tearDown(self):
        """Clean up after the test"""
        del self.my_review

    def test_instance_creation(self):
        """Test the creation of a Review instance"""
        self.assertIsInstance(self.my_review, Review)

    def test_attributes(self):
        """Test the attributes of Review class"""
        self.assertTrue(hasattr(self.my_review, 'place_id'))
        self.assertTrue(hasattr(self.my_review, 'user_id'))
        self.assertTrue(hasattr(self.my_review, 'text'))
        self.assertTrue(hasattr(self.my_review, 'id'))
        self.assertTrue(hasattr(self.my_review, 'created_at'))
        self.assertTrue(hasattr(self.my_review, 'updated_at'))

    def test_types(self):
        """Test the types of Review class attributes"""
        self.assertIsInstance(self.my_review.place_id, str)
        self.assertIsInstance(self.my_review.user_id, str)
        self.assertIsInstance(self.my_review.text, str)
        self.assertIsInstance(self.my_review.id, str)
        self.assertIsInstance(self.my_review.created_at, datetime)
        self.assertIsInstance(self.my_review.updated_at, datetime)

    def test_to_dict_method(self):
        """Test the to_dict method of Review class"""
        review_dict = self.my_review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(type(review_dict['created_at']), str)
        self.assertEqual(type(review_dict['updated_at']), str)

    def test_str_method(self):
        """Test the __str__ method of Review class"""
        string = str(self.my_review)
        self.assertIn("[Review]", string)
        self.assertIn("'id':", string)
        self.assertIn("'created_at':", string)
        self.assertIn("'updated_at':", string)


if __name__ == '__main__':
    unittest.main()
