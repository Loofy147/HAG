import unittest
import torch
import numpy as np
from src.agents.holographic_memory import HolographicWeightEncoder, HolographicLayer
from src.agents.diffusion_reasoning import RecursiveDiffusionReasoning

class TestNovelMechanisms(unittest.TestCase):
    def test_holographic_weight_recovery(self):
        """Test that weights can be recovered after 20% erasure."""
        input_dim, output_dim = 16, 32
        encoder = HolographicWeightEncoder((output_dim, input_dim))
        weights = torch.randn(output_dim, input_dim)

        # Test 20% erasure
        recovered = encoder.recover_weights(weights, erasure_ratio=0.2)

        # Check cosine similarity
        cos_sim = torch.nn.functional.cosine_similarity(
            weights.view(-1), recovered.view(-1), dim=0
        )
        self.assertGreater(cos_sim.item(), 0.8, "Holographic recovery failed to maintain structural integrity.")

    def test_holographic_layer_forward(self):
        """Test forward pass of HolographicLayer under damage."""
        layer = HolographicLayer(16, 8)
        x = torch.randn(1, 16)

        # Normal inference
        out_normal = layer(x, damaged=False)
        # Damaged inference
        out_damaged = layer(x, damaged=True, erasure_ratio=0.2)

        self.assertEqual(out_normal.shape, out_damaged.shape)
        # They shouldn't be identical but should be related
        mse = torch.mean((out_normal - out_damaged)**2)
        self.assertLess(mse.item(), 1.0)

    def test_diffusion_reasoning_convergence(self):
        """Test that recursive diffusion reasoning crystallizes a result."""
        rdr = RecursiveDiffusionReasoning(state_dim=64, num_steps=5)
        initial_state = torch.randn(1, 64)

        final_state = rdr.crystallize(initial_state)

        self.assertEqual(final_state.shape, initial_state.shape)
        # The final state should differ from initial
        self.assertFalse(torch.allclose(initial_state, final_state))

    def test_diffusion_solve_protocol(self):
        """Test the solve_with_diffusion protocol integration."""
        rdr = RecursiveDiffusionReasoning(state_dim=32)
        q_vec = torch.randn(1, 32)
        c_vec = torch.randn(1, 32)
        res = rdr.solve_with_diffusion(q_vec, c_vec)

        self.assertEqual(res["status"], "Crystallized")
        self.assertEqual(res["diffusion_steps"], 10)
        self.assertIn("final_energy", res)

if __name__ == "__main__":
    unittest.main()
