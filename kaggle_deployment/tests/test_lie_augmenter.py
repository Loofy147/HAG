import unittest
import torch
from src.agents.lie_augmenter import LieAugmenter

class TestLieAugmenter(unittest.TestCase):
    def setUp(self):
        self.input_dim = 10
        self.augmenter = LieAugmenter(input_dim=self.input_dim)

    def test_forward_output_shape(self):
        x = torch.randn(5, self.input_dim)
        output = self.augmenter(x)
        # Output should match input shape for augmentation
        self.assertEqual(output.shape, (5, self.input_dim))

    def test_invariance_loss(self):
        x = torch.randn(5, self.input_dim)
        loss = self.augmenter.get_invariance_loss(x)
        self.assertIsInstance(loss, torch.Tensor)
        self.assertEqual(loss.dim(), 0)

if __name__ == "__main__":
    unittest.main()
