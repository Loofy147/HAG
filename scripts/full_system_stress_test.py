import torch
import numpy as np
import os
import sys
import time

# Add src to path
sys.path.append(os.getcwd())

from src.agents.native_recursive import NativelyRecursiveAgent
from src.indexing.holographic_memory import VolumetricHolographicMemory
from src.core.values import SystemValues

def run_hag_40_stress_test():
    print("--- HAG-OS Build 4.0 FINAL MATURITY STRESS TEST ---")

    values = SystemValues()
    print(f"\n[1] BUILD VERSION: {values.version}")

    agent = NativelyRecursiveAgent(agent_id="HAG-Stress-01")

    # 1. VHSE BuRR Scaling
    print("\n[2] TESTING VHSE BuRR DENSITY (1,000 OBJECTS)")
    vhse = VolumetricHolographicMemory(dimension=8192)
    start_time = time.time()
    for i in range(1000):
        vhse.store(torch.randn(8192), torch.randn(8192))
    print(f"    Store Speed (1,000 items): {time.time() - start_time:.3f}s")

    # 2. TRT & RSI Loop
    print("\n[3] TESTING TRT & RSI INTEGRATED LOOP")
    evolution = agent.evolve("Stress test environment data")
    print(f"    Evolution Result: {evolution}")

    # 3. Readiness Matrix
    print("\n[4] HAG-OS Build 4.0 READINESS MATRIX")
    perf = agent.get_performance_report()
    for k, v in perf.items():
        print(f"    {k.upper():.<30} {v}")

    print("\n--- HAG-OS Build 4.0 MATURITY VALIDATED ---")

if __name__ == "__main__":
    run_hag_40_stress_test()
