#!/usr/bin/python3
"""Test for amenity class"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity_attr(self):
        amenity = Amenity()

        # Is created successfully?
        self.assertIsInstance(amenity, Amenity)

        # Does it inherit from BaseModel?
        self.assertIsInstance(amenity, BaseModel)

        # Is "name" attribute present?
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()
