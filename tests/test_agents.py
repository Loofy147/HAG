import unittest
import numpy as np
from src.agents.rlm import RLMOrchestrator
from src.governor.kernel import GovernorKernelEKRLS

class TestRLMOrchestrator(unittest.TestCase):
    def setUp(self):
        self.governor = GovernorKernelEKRLS()
        self.orchestrator = RLMOrchestrator(self.governor)

    def test_context_decomposition_with_peek(self):
        # Small payload: leaf processing
        payload = "A" * 1000
        result = self.orchestrator.process_hypercontext("summarize", payload)
        self.assertEqual(result["orchestration_status"], "Success")
        self.assertEqual(len(result["results"]), 1)
        # Verify REPL state
        self.assertIn("processed_state", result["results"][0])

    def test_recursive_peeking(self):
        # Large payload: 1.5M chars triggers fragmentation
        payload = "B" * 1500000
        result = self.orchestrator.process_hypercontext("analyze", payload)
        self.assertEqual(result["orchestration_status"], "Success")
        # results list should contain dicts with 'peek' and 'recursion'
        self.assertIn("peek", result["results"][0])
        self.assertIn("recursion", result["results"][0])
        self.assertEqual(result["total_tokens"], 1500000)

    def test_repl_state_history(self):
        payload = "C" * 100
        self.orchestrator.process_hypercontext("test_task", payload)
        history = self.orchestrator.repl.history
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["snippet"], "test_task")

if __name__ == '__main__':
    unittest.main()
