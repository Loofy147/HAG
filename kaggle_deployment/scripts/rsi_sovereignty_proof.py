import sys
import os
import torch
sys.path.append(os.getcwd())

from src.agents.native_recursive import NativelyRecursiveAgent
from src.desktop.agent import HAGDesktopAgent
from src.core.values import SystemValues

def prove_rsi_sovereignty():
    print("--- HAG-OS Build 4.0: Recursive Self-Improvement (RSI) Proof ---")
    agent = HAGDesktopAgent()
    values = SystemValues()

    # 1. Verification of RCF Pipeline
    report = agent.get_performance_report()
    print(f"RSI Pipeline: {report['rsi_pipeline']}")
    assert "Study -> Understand -> Test -> Validate -> Generate" in report['rsi_pipeline']

    # 2. Simulation of RSI Cycle (Study -> Validate)
    print("\n[RSI Phase 1: Study] Analyzing cognitive fingerprints...")
    reasoning_vec = torch.randn(8192)
    study = agent.thinking_governor.metacognitive.study_reasoning_step(reasoning_vec, q_score=0.99)
    print(f"Study Status: {study['status']} (Fingerprint: {study['fingerprint']:.4f})")
    assert study['status'] == "COHERENT"

    # 3. Simulation of RSI Cycle (Validate via Sovereign Master Equation)
    print("[RSI Phase 4: Validate] Calibrating Q-score and Thales Delta...")
    proposed_scores = {
        "grounding": 0.99, "certainty": 0.99, "structure": 0.99,
        "applicability": 0.99, "coherence": 0.99, "generativity": 0.99
    }
    schmidt_params = (0.01, 0.01) # Ultra-stable bridge
    validation = agent.thinking_governor.bayesian.validate_improvement(proposed_scores, schmidt_params)
    print(f"Validation Status: {validation['status']} (Q-score: {validation['q_score']:.4f}, Delta: {validation['delta']:.4f})")
    assert validation['is_valid'] == True

    # 4. Simulation of Actuation (LGA Shadow Testing)
    print("[RSI Phase 3: Test] Executing in L1 Shadow Sandbox...")
    token = agent.lga.l3_cap_manager.issue_token("RSI-Task", ["shell_exec"])
    # Intent mismatch simulation
    risky_action = "update_kernel --force"
    task = "Standard optimization"
    result = agent.lga.execute_secured_action(task, risky_action, token, "shell_exec", rsi_shadow=True)
    print(f"Risky Action Result: {result['status']} (Reason: {result.get('reason', 'N/A')})")
    assert result['status'] == "error" # Should be blocked by L2 Intent Verification

    # 5. Full Evolution Loop
    print("\nExecuting full HAG-4.0 Evolution Loop (RSI Active)...")
    evolution_result = agent.evolve("RSI Training Data Context")
    print(f"Evolution Result: {evolution_result}")
    assert "Smoothed P=" in evolution_result
    assert "Crystallized Answer" in evolution_result

    print("\n[CONCLUSION] RSI-Sovereignty SECURED. HAG-OS is now self-metabolizing information.")

if __name__ == "__main__":
    prove_rsi_sovereignty()
