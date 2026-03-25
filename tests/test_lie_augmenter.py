import unittest
import torch
from src.agents.lie_augmenter import LieAugmenter

class TestLieAugmenter(unittest.TestCase):
    def setUp(self):
        self.input_dim = 10
        self.model = LieAugmenter(input_dim=self.input_dim)

    def test_forward_output_shape(self):
        x = torch.randn(5, self.input_dim)
        output = self.model(x)
        self.assertEqual(output.shape, (5, 1))

    def test_invariance_loss_calculation(self):
        x = torch.randn(1, self.input_dim)
        loss = self.model.get_invariance_loss(x)
        self.assertGreaterEqual(loss.item(), 0.0)

    def test_generators_initialization(self):
        self.assertEqual(self.model.generators.shape, (3, self.input_dim, self.input_dim))

if __name__ == '__main__':
    unittest.main()
