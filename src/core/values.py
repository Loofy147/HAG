from dataclasses import dataclass
import json
import os
import numpy as np

@dataclass
class QScoreWeights:
    grounding: float = 0.18
    certainty: float = 0.22
    structure: float = 0.20
    applicability: float = 0.18
    coherence: float = 0.12
    generativity: float = 0.10

class SystemValues:
    """
    Central repository for HAG system constants and Bayesian values.
    Updated for HAG-3.4: Sovereign Master Equation & Thales Diagnostic.
    """
    def __init__(self, config_path="configs/bayesian_weights.json"):
        self.version = "3.4.0-SOVEREIGN"
        self.q_weights = QScoreWeights()
        self.q_threshold = 0.984
        self.snapshot_compression_ratio = 50.0
        self.ram_optimization_target = 0.42
        self.task_accuracy_target = 0.943
        self.aime_accuracy_target = 1.0
        self.error_amplification_limit = 4.4
        self.hallucination_reduction_target = 0.427
        self.weyl_delta_limit = 0.001

        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    w = config.get("Q_Score_Weights", {})
                    self.q_weights = QScoreWeights(
                        grounding=w.get("Grounding", 0.18),
                        certainty=w.get("Certainty", 0.22),
                        structure=w.get("Structure", 0.20),
                        applicability=w.get("Applicability", 0.18),
                        coherence=w.get("Coherence", 0.12),
                        generativity=w.get("Generativity", 0.10)
                    )
                    self.q_threshold = config.get("KF_NG", {}).get("q_threshold", self.q_threshold)
                    self.version = config.get("HAG_Build", {}).get("version", self.version)
            except:
                pass

    def get_aggregate_q_score(self, scores: dict) -> float:
        """Calculates the weighted Q-score based on system values."""
        return (
            scores.get('grounding', 0) * self.q_weights.grounding +
            scores.get('certainty', 0) * self.q_weights.certainty +
            scores.get('structure', 0) * self.q_weights.structure +
            scores.get('applicability', 0) * self.q_weights.applicability +
            scores.get('coherence', 0) * self.q_weights.coherence +
            scores.get('generativity', 0) * self.q_weights.generativity
        )

    def calculate_thales_delta(self, schmidt_x: float, schmidt_y: float) -> float:
        """
        Thales Diagnostic Deficit: delta = 1 - 2*sqrt(xy).
        Used to monitor the stability of 'Reasoning Bridges'.
        """
        h_thales = np.sqrt(schmidt_x * schmidt_y)
        delta = 1.0 - 2.0 * h_thales
        return delta

    def calculate_calm_harmony(self, authority: float, liberty: float, alpha=0.5, beta=0.5, gamma=0.2) -> float:
        """
        C-ALM Harmony Functional: H(A,L) = alpha*f(A) + beta*g(L) - gamma*C(A,L).
        Balances sovereignty (Authority) and information flow (Liberty).
        """
        harmony = alpha * authority + beta * liberty - gamma * (authority * liberty)
        return harmony

    def verify_sovereignty_master_equation(self, scores: dict, schmidt_params: tuple) -> bool:
        """
        Sovereign Master Equation Check: Q subject to delta > 0.
        """
        q_score = self.get_aggregate_q_score(scores)
        delta = self.calculate_thales_delta(*schmidt_params)

        # Stability Condition: Q > q_threshold AND delta > weyl_delta_limit
        return q_score >= self.q_threshold and delta > self.weyl_delta_limit
