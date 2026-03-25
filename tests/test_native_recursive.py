import unittest
import torch
from src.agents.native_recursive import NativelyRecursiveAgent

class TestRLMNative(unittest.TestCase):
    def setUp(self):
        self.agent = NativelyRecursiveAgent()

    def test_solve_complex_task(self):
        query = "Find the logic hidden in 10M tokens"
        context = "A massive 10M token context simulated as a string."

        # Test basic execution flow
        result = self.agent.solve_complex_task(query, context)
        self.assertIn("synthesized from 1 RLM-N sub-calls", result)

    def test_performance_metrics(self):
        report = self.agent.get_performance_report()
        self.assertEqual(report["context_capacity"], "10M+ Tokens (100x Growth)")
        self.assertEqual(report["retrieval_accuracy"], "62% (Target)")

if __name__ == '__main__':
    unittest.main()
