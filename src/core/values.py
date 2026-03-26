from dataclasses import dataclass
import json
import os

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
    Updated for HAG-3.0: Evolutionary Sovereignty.
    """
    def __init__(self, config_path="configs/bayesian_weights.json"):
        self.version = "3.0.0-PROTOTYPE"
        self.q_weights = QScoreWeights()
        self.q_threshold = 0.943 # Updated for HAG-3.0 precision
        self.snapshot_compression_ratio = 50.0 # 50:1 Target

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
                    self.q_threshold = config.get("EKRLS", {}).get("q_threshold", self.q_threshold)
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
