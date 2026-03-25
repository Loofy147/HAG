import unittest
from src.indexing.ribbon import RibbonIndexer

class TestRibbonIndexer(unittest.TestCase):
    def setUp(self):
        self.indexer = RibbonIndexer(capacity=1000)

    def test_insertion_lookup(self):
        key = "particle_entanglement_pair_42"
        metadata = {"spin": "up", "coordinates": [1, 2, 3]}
        self.assertTrue(self.indexer.insert(key, metadata))

        retrieved = self.indexer.lookup(key)
        self.assertEqual(retrieved, metadata)

    def test_memory_optimization_report(self):
        report = self.indexer.get_memory_usage()
        self.assertIn("27%", report)

if __name__ == '__main__':
    unittest.main()
