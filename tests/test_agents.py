import unittest
import numpy as np
from src.agents.rlm import RLMOrchestrator
from src.governor.kernel import GovernorKernelEKRLS

class TestRLMOrchestrator(unittest.TestCase):
    def setUp(self):
        self.governor = GovernorKernelEKRLS()
        self.orchestrator = RLMOrchestrator(self.governor)

    def test_context_decomposition(self):
        # Small payload: should be leaf
        payload = "A" * 1000
        result = self.orchestrator.process_hypercontext("summarize", payload)
        self.assertEqual(result["orchestration_status"], "Success")
        self.assertEqual(len(result["results"]), 1)
        self.assertEqual(result["total_tokens"], 1000)

    def test_recursive_decomposition(self):
        # Large payload: should fragment (threshold 1M)
        payload = "B" * 1500000
        result = self.orchestrator.process_hypercontext("analyze", payload)
        self.assertEqual(result["orchestration_status"], "Success")
        # Should have split once: results[0] and results[1] (both under 1M)
        self.assertEqual(len(result["results"]), 2)
        self.assertEqual(result["total_tokens"], 1500000)

    def test_performance_report(self):
        payload = "C" * 10000
        self.orchestrator.process_hypercontext("test", payload)
        report = self.orchestrator.get_performance_report()
        self.assertEqual(report["tokens_processed"], 10000)
        self.assertGreater(report["estimated_token_savings"], 0)

if __name__ == '__main__':
    unittest.main()
