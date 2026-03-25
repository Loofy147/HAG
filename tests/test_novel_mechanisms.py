import unittest
import torch
import numpy as np
from src.agents.holographic_memory import HolographicWeightEncoder, HolographicLayer
from src.agents.diffusion_reasoning import RecursiveDiffusionReasoning
from src.agents.resilient_model import ResilientHAGModel
from src.agents.native_recursive import NativelyRecursiveAgent

class TestNovelMechanisms(unittest.TestCase):
    def test_holographic_weight_recovery(self):
        """Test that weights can be recovered after 20% erasure."""
        input_dim, output_dim = 16, 32
        encoder = HolographicWeightEncoder((output_dim, input_dim))
        weights = torch.randn(output_dim, input_dim)

        recovered = encoder.recover_weights(weights, erasure_ratio=0.2)

        cos_sim = torch.nn.functional.cosine_similarity(
            weights.view(-1), recovered.view(-1), dim=0
        )
        self.assertGreater(cos_sim.item(), 0.8, "Holographic recovery failed to maintain structural integrity.")

    def test_diffusion_reasoning_convergence(self):
        """Test that recursive diffusion reasoning crystallizes a result."""
        rdr = RecursiveDiffusionReasoning(state_dim=64, num_steps=5)
        q_vec = torch.randn(1, 32)
        c_vec = torch.randn(1, 32)
        res = rdr.solve_with_diffusion(q_vec, c_vec)

        self.assertEqual(res["status"], "Crystallized")
        self.assertEqual(res["diffusion_steps"], 5)
        self.assertIn("final_energy", res)

    def test_resilient_hag_model_forward(self):
        """Test the ResilientHAGModel forward pass and resilience report."""
        model = ResilientHAGModel(input_dim=16)
        x = torch.randn(2, 16)

        # Test forward
        y = model(x, damaged=True, erasure_ratio=0.2)
        self.assertEqual(y.shape, (2, 1))

        # Test report
        report = model.get_resilience_report(x, erasure_ratio=0.2)
        self.assertIn("recovery_precision", report)
        self.assertIn("invariance_loss", report)

    def test_native_recursive_agent_crystallization(self):
        """Test NativelyRecursiveAgent integration with Diffusion."""
        agent = NativelyRecursiveAgent()
        massive_input = "Test input data for RLM-N analysis."
        answer = agent.solve_complex_task("Query", massive_input)

        self.assertIn("Crystallized Answer", answer)
        self.assertIn("RLM-N sub-calls", answer)

if __name__ == "__main__":
    unittest.main()
