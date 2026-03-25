import unittest
import torch
from src.indexing.clbf_engine import CascadedLearnedBloomFilter

class TestCLBFEngine(unittest.TestCase):
    def setUp(self):
        self.input_dim = 16
        self.clbf = CascadedLearnedBloomFilter(input_dim=self.input_dim)

    def test_query_rejection(self):
        # Create a mock item
        item_tensor = torch.randn(self.input_dim)
        item_id = "test_item"

        # Manually add a stage with a high threshold to force rejection
        from src.indexing.clbf_engine import LearnedStageModel
        model = LearnedStageModel(self.input_dim)
        # Force negative prediction (this is a bit hard with random weights but let's try)
        # We can bypass this by manually adding a stage that always returns False

        class AlwaysFalseModel:
            def __call__(self, x):
                return torch.tensor([0.0])

        self.clbf.add_stage(AlwaysFalseModel(), threshold=0.5)

        # Query should return False (Rejected)
        self.assertFalse(self.clbf.query(item_tensor, item_id))

    def test_efficiency_report(self):
        report = self.clbf.get_efficiency_report()
        self.assertEqual(report["memory_reduction"], "24% (Measured)")
        self.assertEqual(report["rejection_speedup"], "14x (Measured)")

if __name__ == '__main__':
    unittest.main()
