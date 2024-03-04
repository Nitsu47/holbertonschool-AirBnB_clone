#!/usr/bin/python3
"""Test for State class"""
import unittest
from models.basemodel import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    def teststateattr(self):
        state = State()

        # Is created successfully?
        self.assertIsInstance(state, State)

        # Does it inherit from BaseModel?
        self.assertIsInstance(state, BaseModel)

        # Is "name" attribute present?
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

if _name == '__main':
    unittest.main()
