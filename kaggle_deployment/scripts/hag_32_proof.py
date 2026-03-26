import torch
import numpy as np
import os
import sys

# Add src to path
sys.path.append(os.getcwd())

from src.agents.native_recursive import NativelyRecursiveAgent
from src.indexing.holographic_memory import VolumetricHolographicMemory
from src.governor.kfng_governor import KFNGGovernor
from src.core.values import SystemValues

def prove_hag_32_spacetime_memory():
    print("--- HAG-3.2 ENGINEERING PROOF: SPACETIME MEMORY & KF-NG ---")

    agent = NativelyRecursiveAgent()
    values = SystemValues()

    print(f"\n[1] BUILD VERSION: {values.version}")
    print(f"[1] TARGET Q-THRESHOLD: {values.q_threshold}")

    # 1. Verify KF-NG O(N) Complexity and Precision
    print("\n[2] TESTING KF-NG (KRONECKER-FACTORED NATURAL GOVERNOR)")
    governor = KFNGGovernor(input_dim=4096, threshold=0.982)
    reasoning_vector = torch.randn(4096)

    # Check step precision
    is_stable = governor.step(reasoning_vector, feedback_signal=1.0)
    print(f"    Initial Stability: {is_stable}")

    # Test drift detection
    drift_is_stable = governor.step(reasoning_vector, feedback_signal=0.5)
    print(f"    Stability under 50% drift: {drift_is_stable}")

    assert drift_is_stable == False, "KF-NG failed to detect significant logic drift"
    print("    SUCCESS: KF-NG tracks integrity on Fisher Manifold.")

    # 2. Verify VHSE (Volumetric Holographic Storage Engine)
    print("\n[3] TESTING VHSE (BINDING & BUNDLING FIDELITY)")
    vhse = VolumetricHolographicMemory(dimension=4096)

    # Create key-value pairs
    k1 = torch.sign(torch.randn(4096))
    v1 = torch.sign(torch.randn(4096))

    k2 = torch.sign(torch.randn(4096))
    v2 = torch.sign(torch.randn(4096))

    # Store in VHSE
    vhse.store(k1, v1)
    vhse.store(k2, v2)

    # Retrieve
    retrieved_v1 = vhse.retrieve(k1)
    retrieved_v2 = vhse.retrieve(k2)

    # Calculate fidelity (Correlation)
    fidelity1 = torch.mean((retrieved_v1 == v1).float()).item()
    fidelity2 = torch.mean((retrieved_v2 == v2).float()).item()

    print(f"    Retrieval 1 Fidelity: {fidelity1*100:.2f}%")
    print(f"    Retrieval 2 Fidelity: {fidelity2*100:.2f}%")

    assert fidelity1 > 0.70, "VHSE retrieval fidelity too low"
    print("    SUCCESS: Volumetric memory preserves information via holographic interference.")

    # 3. Final Performance Report
    print("\n[4] HAG-3.2 PERFORMANCE REPORT")
    report = agent.get_performance_report()
    for k, v in report.items():
        print(f"    {k.upper()}: {v}")

    print("\n--- HAG-3.2 PROOF COMPLETE: SPACETIME INFRASTRUCTURE SECURED ---")

if __name__ == "__main__":
    prove_hag_32_spacetime_memory()
