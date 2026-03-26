import sys
import os
sys.path.append(os.getcwd())

from src.desktop.agent import HAGDesktopAgent
from src.core.values import SystemValues

def prove_desktop_sovereignty():
    print("--- HAG-Desktop Build 4.0: Sovereign Master Proof ---")
    agent = HAGDesktopAgent()
    values = SystemValues()

    # 1. Verification of System Version
    print(f"System Version: {values.version}")
    assert "4.0.0" in values.version

    # 2. Verification of Multimodal Perception
    perception = agent.perception.get_desktop_context()
    print(f"Perception Mode: {perception['perception_mode']}")
    assert perception['perception_mode'] == "MULTIMODAL_SOVEREIGN"

    # 3. Verification of Secured Execution (LGA)
    print("Executing Sovereign Task: 'Summarize local logs'")
    task_result = agent.execute_desktop_task("Summarize local logs and find errors")

    print(f"Task Result Status: {task_result['result']['status']}")
    print(f"LGA Verification: {task_result['governance']}")
    assert task_result['result']['status'] == "success"
    assert "LGA" in task_result['governance']

    # 4. Operational Formula Proof (E_desktop)
    print(f"Calculated E_desktop: {task_result['e_desktop']:.2f}")
    assert task_result['e_desktop'] > values.e_desktop_stable_threshold

    # 5. Readiness Summary
    report = agent.get_desktop_readiness_report()
    print("\n--- Readiness Matrix (Build 4.0) ---")
    for k, v in report.items():
        if isinstance(v, (str, float, int)):
             print(f"{k:.<30} {v}")

    print("\n[CONCLUSION] HAG-Desktop Build 4.0 SECURED. SOVEREIGNTY ACHIEVED.")

if __name__ == "__main__":
    prove_desktop_sovereignty()
