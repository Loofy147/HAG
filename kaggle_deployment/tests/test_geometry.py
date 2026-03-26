import unittest
import numpy as np
from src.geometry.engine import SpacetimeEngine

class TestSpacetimeEngine(unittest.TestCase):
    def setUp(self):
        self.engine = SpacetimeEngine(alpha=1.0)

    def test_metric_tensor_hessian(self):
        # Sample entropy function: S = x^2 + y^2
        # Hessian should be [[2, 0], [0, 2]]
        def sample_entropy(coords):
            return np.sum(coords**2)

        coords = np.array([1.0, 1.0])
        metric = self.engine.compute_metric_tensor(sample_entropy, coords)

        expected = np.array([[2.0, 0.0], [0.0, 2.0]])
        np.testing.assert_allclose(metric, expected, atol=1e-4)

    def test_bridge_stability(self):
        # Case 1: Stable (h = sqrt(0.1*0.1) = 0.1, delta = 1 - 0.2 = 0.8 > 0)
        stable_result = self.engine.check_bridge_stability(0.1, 0.1)
        self.assertTrue(stable_result["is_stable"])
        self.assertAlmostEqual(stable_result["entanglement_deficit"], 0.8)

        # Case 2: Unstable (h = sqrt(0.3*0.3) = 0.3, delta = 1 - 0.6 = 0.4 > 0? No, h=0.6, delta=-0.2)
        # Wait, if h=0.6, delta = 1 - 1.2 = -0.2.
        unstable_result = self.engine.check_bridge_stability(0.6, 0.6)
        # h = 0.6, delta = 1 - 1.2 = -0.2
        self.assertFalse(unstable_result["is_stable"])
        self.assertLess(unstable_result["entanglement_deficit"], 0)

    def test_emergent_volume(self):
        metric = np.array([[4.0, 0.0], [0.0, 9.0]])
        # det = 36, sqrt(det) = 6
        volume = self.engine.get_emergent_volume(metric)
        self.assertEqual(volume, 6.0)

if __name__ == '__main__':
    unittest.main()
