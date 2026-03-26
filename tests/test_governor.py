import unittest
import numpy as np
from src.governor.governor import HolographicGovernor

class TestHolographicGovernor(unittest.TestCase):
    def setUp(self):
        # High threshold to prevent early exits during initialization steps
        self.governor = HolographicGovernor(lambda_forget=0.99, sigma_kernel=1.0, threshold=0.0)

    def test_initial_step(self):
        vec = np.array([1.0, 1.0])
        status = self.governor.step(vec, 1.0)
        self.assertTrue(status)
        self.assertEqual(len(self.governor.dictionary), 1)

    def test_drift_detection(self):
        # 1. Initialize with stable state
        self.governor.threshold = 0.85
        self.governor.step(np.array([1.0, 1.0]), 1.0)

        # 2. Trigger drift (Large error)
        # Prediction for [2, 2] will be near 1.0, but we provide feedback 0.0
        vec_drift = np.array([2.0, 2.0])
        status = self.governor.step(vec_drift, 0.0)

        # If error > 1 - 0.85 (0.15), should return False
        self.assertFalse(status)

    def test_recursive_update_stability(self):
        # 1. Initialize with stable state
        self.governor.threshold = 0.0 # Don't detect drift

        # Multiple steps to check dictionary growth
        count = 0
        for i in range(5):
            vec = np.random.randn(2)
            if self.governor.step(vec, 1.0):
                count += 1

        # Check total items in dictionary
        self.assertEqual(len(self.governor.dictionary), 5)
        # Check that matrices are at least as large as the active items
        self.assertGreaterEqual(self.governor.Q.shape[0], 5)

if __name__ == '__main__':
    unittest.main()
