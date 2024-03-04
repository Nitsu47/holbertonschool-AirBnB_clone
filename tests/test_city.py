#!/usr/bin/python3
"""Test for city class"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city_attr(self):
        city = City()

        # Is created successfully?
        self.assertIsInstance(city, City)

        # Does it inherit from BaseModel?
        self.assertIsInstance(city, BaseModel)

        # Is "name" attribute present?
        self.assertTrue(hasattr(city, 'name'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

if __name__ == '__main__':
    unittest.main()
