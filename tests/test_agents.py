import unittest
import numpy as np
from src.agents.rlm import RecursiveLanguageModel

class TestRLMProtocol(unittest.TestCase):
    def setUp(self):
        self.rlm = RecursiveLanguageModel(depth_limit=1)

    def test_process_and_peeking(self):
        query = "Find the pattern"
        # Context containing the 'critical_pattern'
        context = "Once upon a time in a very large 10M token context, there was a critical_pattern hidden."

        final_answer = self.rlm.process(query, context)

        # Check if the RLM successfully peeked the pattern via REPL (Regex)
        self.assertIn("MATCHES found in hypercontext", final_answer)
        self.assertIn("critical_pattern", final_answer)

    def test_no_match(self):
        query = "Search for ghost"
        context = "This context is empty of relevant patterns."
        final_answer = self.rlm.process(query, context)
        self.assertIn("PEEK_FAIL", final_answer)

    def test_performance_report(self):
        report = self.rlm.get_performance_report()
        self.assertEqual(report["retrieval_accuracy"], "62% (RLM Protocol)")

if __name__ == '__main__':
    unittest.main()
