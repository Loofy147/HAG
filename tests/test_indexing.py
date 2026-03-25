import unittest
from src.indexing.ribbon import RibbonIndexer

class TestRibbonIndexer(unittest.TestCase):
    def setUp(self):
        # Small capacity for testing
        self.indexer = RibbonIndexer(capacity=1000, ribbon_width=16)

    def test_insertion_lookup(self):
        key = "particle_entanglement_pair_42"
        metadata = {"spin": "up", "coordinates": [1, 2, 3]}
        self.assertTrue(self.indexer.insert(key, metadata))

        retrieved = self.indexer.lookup(key)
        self.assertEqual(retrieved, metadata)

    def test_ribbon_structure(self):
        # Verify bit-array allocation
        self.assertEqual(len(self.indexer.matrix), 1100) # 1000 * 1.1

    def test_memory_optimization_report(self):
        report = self.indexer.get_memory_usage()
        # Ensure savings is over 27% (in this model: 1 - (1100*64 / 1000*256) = 1 - 0.275 = 72.5%)
        savings_str = report["memory_savings"]
        savings_val = float(savings_str.split('%')[0])
        self.assertGreater(savings_val, 27.0)

if __name__ == '__main__':
    unittest.main()
