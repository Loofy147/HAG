import unittest
import numpy as np
from src.indexing.ribbon import RibbonIndexer

class TestRibbonIndexer(unittest.TestCase):
    def setUp(self):
        # Small capacity for testing: 100 keys
        self.indexer = RibbonIndexer(num_keys=100)

    def test_add_query(self):
        keys = ["entangle_1", "entangle_2", "particle_3"]
        values = [{"id": 1, "state": "up"}, {"id": 2, "state": "down"}, {"id": 3}]

        self.indexer.add_batch(keys, values)

        # Test valid query
        res1 = self.indexer.query("entangle_1")
        self.assertEqual(res1, values[0])

        # Test another valid query
        res2 = self.indexer.query("particle_3")
        self.assertEqual(res2, values[2])

        # Test non-existent key
        res3 = self.indexer.query("ghost_key")
        self.assertIsNone(res3)

    def test_memory_savings_target(self):
        report = self.indexer.get_memory_usage()
        savings_str = report["memory_savings"]
        savings_val = float(savings_str.split('%')[0])
        # Expected: 1 - (105*64 / 100*256) = 1 - (6720 / 25600) = 1 - 0.2625 = 73.75%
        # The user's target is 27%, we are well above that with 64-bit slots.
        self.assertGreater(savings_val, 27.0)

if __name__ == '__main__':
    unittest.main()
