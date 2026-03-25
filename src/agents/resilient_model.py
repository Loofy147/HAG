import torch
import torch.nn as nn
from src.agents.lie_augmenter import LieAugmenter
from src.agents.holographic_memory import HolographicLayer

class ResilientHAGModel(nn.Module):
    """
    نموذج HAG المرن (Build 2.1).
    ResilientHAGModel: Combines Symmetry-Aware Feature Extraction (LieAugmenter)
    with Robust Holographic Weight Storage.
    """
    def __init__(self, input_dim, hidden_dim=64):
        super().__init__()
        # 1. Symmetry discovery for data efficiency (40% target)
        # Note: LieAugmenter takes input_dim and returns transformed input_dim
        self.symmetry_engine = LieAugmenter(input_dim=input_dim, hidden_dim=hidden_dim)

        # 2. Holographic resilience layer
        # robust_layer input_dim should match the output of symmetry_engine (which is input_dim)
        self.robust_layer = HolographicLayer(input_dim, hidden_dim)

        # 3. Final prediction
        self.final_net = nn.Sequential(
            nn.ReLU(),
            nn.Linear(hidden_dim, 1)
        )

    def forward(self, x, damaged=False, erasure_ratio=0.2):
        """
        Forward pass with optional weight erasure simulation.
        """
        # Symmetry-aware input augmentation: Returns (batch, input_dim)
        augmented_x = self.symmetry_engine(x)

        # Process through robust layer: (batch, input_dim) -> (batch, hidden_dim)
        h = self.robust_layer(augmented_x, damaged=damaged, erasure_ratio=erasure_ratio)

        # Final output: (batch, 1)
        return self.final_net(h)

    def get_resilience_report(self, x, erasure_ratio=0.2):
        """
        Calculates model performance degradation under synaptic erasure.
        """
        y_orig = self.forward(x, damaged=False)
        y_damaged = self.forward(x, damaged=True, erasure_ratio=erasure_ratio)

        # Recovery precision (1 - error)
        error = torch.mean((y_orig - y_damaged)**2).item()
        recovery_precision = 1.0 - error if error < 1.0 else 0.0

        # Symmetry invariance
        invariance_loss = self.symmetry_engine.get_invariance_loss(x).item()

        return {
            "recovery_precision": recovery_precision,
            "invariance_loss": invariance_loss,
            "status": "SECURE" if recovery_precision > 0.8 else "VULNERABLE"
        }
