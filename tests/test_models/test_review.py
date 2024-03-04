#!/usr/bin/python3
"""Test for Review class"""
import unittest
from models.base_model import BaseModel
from models.review import Review

class TestState(unittest.TestCase):
    def test_review_attr(self):
        review = Review()

        # Is created successfully?
        self.assertIsInstance(review, Review)

        # Does it inherit from BaseModel?
        self.assertIsInstance(review, BaseModel)

        # Are attributes present?
        self.assertTrue(hasattr(state, 'name'))
        self.assertTrue(hasattr(state, 'place_id'))
        self.assertTrue(hasattr(state, 'user_id'))
        
        self.assertEqual(state.name, "")
        self.assertEqual(state.place_id, "")
        self.assertEqual(state.user_id, "")

if __name__ == '__main__':
    unittest.main()
