import unittest
import numpy as np
from src.governor.kernel import GovernorKernelEKRLS

class TestGovernorKernel(unittest.TestCase):
    def setUp(self):
        self.governor = GovernorKernelEKRLS(lambda_reg=0.1, sigma=1.0)

    def test_initial_update(self):
        # Initial step
        step = np.array([0.1, 0.2, 0.3])
        feedback = 1.0
        integrity = self.governor.update_integrity(step, feedback)
        self.assertEqual(integrity, 1.0)
        self.assertEqual(len(self.governor.dictionary), 1)
        self.assertEqual(self.governor.Q.shape, (1, 1))

    def test_integrity_drift(self):
        # Initial step
        step1 = np.array([0.0, 0.0, 0.0])
        self.governor.update_integrity(step1, 1.0)

        # Step with drift (lower integrity)
        step2 = np.array([5.0, 5.0, 5.0]) # Far from step1
        feedback = 0.1 # Very different from step1
        integrity = self.governor.update_integrity(step2, feedback)

        # Integrity should be less than 1.0 due to the large step difference
        self.assertLess(integrity, 1.0)
        self.assertEqual(len(self.governor.dictionary), 2)
        self.assertEqual(self.governor.Q.shape, (2, 2))

if __name__ == '__main__':
    unittest.main()
