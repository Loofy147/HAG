import unittest
import torch
import os
from src.agents.data_loader import GeneralDataLoader

class TestGeneralDataLoader(unittest.TestCase):
    def setUp(self):
        self.loader = GeneralDataLoader(input_dim=16)

    def test_physics_load(self):
        x, y = self.loader.load_domain_data(domain="physics")
        if x is not None:
            self.assertEqual(x.shape[1], 16)
            self.assertGreater(x.shape[0], 0)
        else:
            self.skipTest("Physics data not found.")

    def test_finance_load(self):
        x, y = self.loader.load_domain_data(domain="finance")
        if x is not None:
            self.assertEqual(x.shape[1], 16)
            self.assertGreater(x.shape[0], 0)
        else:
            self.skipTest("Finance data not found.")

if __name__ == "__main__":
    unittest.main()
