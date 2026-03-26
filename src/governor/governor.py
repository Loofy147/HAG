import numpy as np
import json
import os
from src.core.values import SystemValues

class HolographicGovernor:
    """
    محرك Governor 2.1 (HAG-2.1) لتتبع نزاهة الاستدلال.
    HolographicGovernor: Tracks reasoning integrity and prevents model drift via EKRLS.
    """
    def __init__(self, config_path="configs/bayesian_weights.json", **kwargs):
        self.values = SystemValues(config_path)
        self.lam = kwargs.get('lambda_forget', 0.99)
        self.sigma = kwargs.get('sigma_kernel', 1.0)

        # Load specific EKRLS params from file if not overridden by kwargs
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    ekrls = config.get("EKRLS", {})
                    if 'sigma_kernel' not in kwargs:
                        self.sigma = ekrls.get("sigma", self.sigma)
            except:
                pass

        self.Q = None
        self.alpha = None
        self.dictionary = []
        # Use explicit threshold if provided, else use system values
        self.threshold = kwargs.get('threshold', self.values.q_threshold)

    def _compute_kernel_vector(self, reasoning_vector):
        if not self.dictionary: return np.array([])
        # ⚡ Optimization: Vectorized distance computation (Bolt)
        # Replaces: np.array([np.linalg.norm(reasoning_vector - d)**2 for d in self.dictionary])
        diffs = np.sum((np.array(self.dictionary) - reasoning_vector)**2, axis=1)
        return np.exp(-diffs / (2 * self.sigma**2))

    def step(self, reasoning_vector, feedback_signal):
        h = self._compute_kernel_vector(reasoning_vector)
        if self.Q is None:
            self.Q = np.array([[1.0 / (self.lam + 1.0)]])
            self.alpha = np.array([feedback_signal / (self.lam + 1.0)])
            self.dictionary.append(reasoning_vector)
            return True

        z = self.Q @ h
        r = self.lam + 1.0 - h.T @ z
        prediction = h.T @ self.alpha
        prediction_error = feedback_signal - prediction

        if abs(prediction_error) > (1.0 - self.threshold):
            self._trigger_metacognitive_reflection(prediction_error)
            return False

        # ⚡ Fix: Correct dimension expansion for EKRLS (Bolt)
        # We need to grow Q and alpha when adding a new dictionary element
        m = self.Q.shape[0]
        new_Q = np.zeros((m + 1, m + 1))
        new_Q[:m, :m] = self.Q + np.outer(z, z) / r
        new_Q[:m, m] = -z / r
        new_Q[m, :m] = -z / r
        new_Q[m, m] = 1.0 / r
        self.Q = new_Q

        new_alpha = np.zeros(m + 1)
        new_alpha[:m] = self.alpha - (z / r) * prediction_error
        new_alpha[m] = prediction_error / r
        self.alpha = new_alpha

        self.dictionary.append(reasoning_vector)
        return True

    def _trigger_metacognitive_reflection(self, error):
        print(f"ALERT: Reasoning Drift Detected (Error: {error:.4f}). Initiating Suffix Smoothing Protocol...")
