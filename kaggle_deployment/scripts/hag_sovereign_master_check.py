import sys
import os
import torch
import numpy as np
sys.path.append(os.getcwd())

from src.core.values import SystemValues
from src.agents import *
from src.governor import *
from src.indexing import *
from src.desktop import *

def run_master_check():
    print("=== HAG-OS Build 4.0: Sovereign Master Check ===")
    values = SystemValues()
    print(f"System Version: {values.version}")

    components = [
        ("VHSE", VolumetricHolographicMemory(dimension=128)),
        ("KF-NG", KFNGGovernor(input_dim=128)),
        ("ThinkingGovernor", ThinkingGovernor()),
        ("Ribbon", RibbonIndexer(num_keys=100)),
        ("CLBF", CascadedLearnedBloomFilter(input_dim=16)),
        ("LieAugmenter", LieAugmenter(input_dim=16)),
        ("LGA", LayeredGovernance(agent_id="Master-Check")),
        ("DesktopAgent", HAGDesktopAgent())
    ]

    all_ok = True
    print("\n--- Component Metadata & Signature Audit ---")
    for name, comp in components:
        try:
            report = {}
            if hasattr(comp, "get_performance_report"): report = comp.get_performance_report()
            elif hasattr(comp, "get_efficiency_report"): report = comp.get_efficiency_report()
            elif hasattr(comp, "get_memory_usage"): report = comp.get_memory_usage()
            elif hasattr(comp, "get_symmetry_metrics"): report = comp.get_symmetry_metrics()
            elif hasattr(comp, "get_kfng_metrics"): report = comp.get_kfng_metrics()
            elif hasattr(comp, "get_desktop_readiness_report"): report = comp.get_desktop_readiness_report()

            version = report.get("version", "N/A")
            print(f"[OK] {name:.<20} Version: {version}")

            if version != "N/A" and "4.0.0" not in version:
                print(f"     [!] Version Mismatch: {version}")
                all_ok = False
        except Exception as e:
            print(f"[FAIL] {name:.<20} Error: {e}")
            all_ok = False

    if all_ok:
        print("\n[CONCLUSION] ALL SYSTEMS HARMONIZED. Build 4.0 is self-consistent.")
    else:
        print("\n[CONCLUSION] HARMONIZATION FAILED. Audit required.")
        sys.exit(1)

if __name__ == "__main__":
    run_master_check()
