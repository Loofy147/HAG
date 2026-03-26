import unittest
import torch
from src.agents.native_recursive import NativelyRecursiveAgent

class TestRLMNative(unittest.TestCase):
    def setUp(self):
        self.agent = NativelyRecursiveAgent()

    def test_solve_complex_task(self):
        query = "Extract all instances of 'pattern' in the data."
        massive_input = "Sample data with critical_pattern and another snippet."
        result = self.agent.solve_complex_task(query, massive_input)

        # Build 2.1 uses Crystallization
        self.assertIn("Crystallized Answer", result)
        self.assertIn("RLM-N sub-calls", result)

    def test_performance_report(self):
        report = self.agent.get_performance_report()
        self.assertEqual(report["context_capacity"], "10M+ Tokens (100x Growth)")
        self.assertEqual(report["retrieval_accuracy"], "62% (Target)")
        self.assertEqual(report["token_efficiency"], "3.0x (Target)")

if __name__ == "__main__":
    unittest.main()
