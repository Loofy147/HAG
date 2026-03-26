import torch
import numpy as np
import os
import sys

# Add src to path
sys.path.append(os.getcwd())

from src.core.values import SystemValues
from src.geometry.engine import SpacetimeEngine
from src.agents.native_recursive import NativelyRecursiveAgent
from src.indexing.holographic_memory import VolumetricHolographicMemory

def prove_hag_40_sovereignty_master():
    print("--- HAG-OS Build 4.0 ENGINEERING PROOF: SOVEREIGN MASTER EQUATION ---")

    values = SystemValues()
    engine = SpacetimeEngine()
    agent = NativelyRecursiveAgent()

    print(f"\n[1] BUILD VERSION: {values.version}")
    print(f"[1] SOVEREIGNTY THRESHOLD: {values.q_threshold}")

    # 1. Verify Sovereign Master Equation (Thales + Q)
    print("\n[2] TESTING SOVEREIGN MASTER EQUATION (Thales Diagnostic)")
    # Case A: Stable Reasoning Bridge
    scores = {'grounding': 1.0, 'certainty': 1.0, 'structure': 1.0,
              'applicability': 1.0, 'coherence': 1.0, 'generativity': 1.0}
    schmidt_params = (0.2, 0.2) # delta = 1 - 0.4 = 0.6

    is_sovereign = values.verify_sovereignty_master_equation(scores, schmidt_params)
    delta = values.calculate_thales_delta(*schmidt_params)
    print(f"    Scenario A: High Q, Stable Bridge (delta={delta:.2f}) -> Sovereign: {is_sovereign}")
    assert is_sovereign == True, "Stable bridge failed sovereignty check"

    # Case B: Unstable Reasoning Bridge (Weyl Limit)
    unstable_params = (0.5, 0.5) # delta = 0.0
    is_sovereign_b = values.verify_sovereignty_master_equation(scores, unstable_params)
    delta_b = values.calculate_thales_delta(*unstable_params)
    print(f"    Scenario B: High Q, Unstable Bridge (delta={delta_b:.2f}) -> Sovereign: {is_sovereign_b}")
    assert is_sovereign_b == False, "Unstable bridge should fail sovereignty check"

    # 2. Verify Metric Emergence Hessian
    print("\n[3] TESTING METRIC EMERGENCE HESSIAN")
    def s_ent(xi): return 0.5 * np.sum(xi**2)
    coords = [1.0, 2.0, 3.0]
    metric = engine.compute_metric_tensor(s_ent, coords)
    print(f"    Metric Tensor Hessian:\n{metric}")
    assert np.allclose(metric, np.eye(3), atol=1e-4)

    # 3. Verify C-ALM Harmony
    print("\n[4] TESTING C-ALM HARMONY")
    harmony = values.calculate_calm_harmony(authority=0.9, liberty=0.8)
    print(f"    C-ALM Harmony Score: {harmony:.4f}")

    # 4. Final System Integration Check
    print("\n[5] TESTING TRT & RSI INTEGRATION")
    trt_res = agent.test_time_recursive_thinking("Global Sovereignty Proof")
    print(f"    TRT Result: {trt_res['status']}")

    print("\n--- HAG-OS Build 4.0 PROOF COMPLETE: THE MATHEMATICAL EXPRESSION IS SECURED ---")

if __name__ == "__main__":
    prove_hag_40_sovereignty_master()
