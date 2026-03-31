import sys
import os
sys.path.append(os.getcwd())

def verify_bundle():
    print("--- HAG-Desktop Build 4.0: Bundle Verification ---")

    modules_to_test = [
        "src.core.values",
        "src.agents.native_recursive",
        "src.desktop.governance",
        "src.desktop.binding",
        "src.desktop.perception",
        "src.desktop.agent",
        "src.cli.main"
    ]

    all_passed = True
    for mod in modules_to_test:
        try:
            __import__(mod)
            print(f"[PASS] Imported: {mod}")
        except ImportError as e:
            print(f"[FAIL] Failed to import: {mod} ({e})")
            all_passed = False

    # Check version in values
    from src.core.values import SystemValues
    values = SystemValues()
    print(f"Detected Version: {values.version}")

    if "4.0.1" not in values.version:
        print("[FAIL] Version mismatch!")
        all_passed = False

    # Check CLI integration
    import subprocess
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = os.getcwd()
        result = subprocess.run(["python3", "src/cli/main.py", "--help"], capture_output=True, text=True, env=env)
        if "--desktop" in result.stdout:
            print("[PASS] CLI --desktop flag detected")
        else:
            print("[FAIL] CLI --desktop flag MISSING")
            print(f"Output: {result.stdout}")
            print(f"Error: {result.stderr}")
            all_passed = False
    except Exception as e:
        print(f"[FAIL] CLI Help test failed: {e}")
        all_passed = False

    if all_passed:
        print("\n[CONCLUSION] Bundle Verification SUCCESSFUL. Ready for submission.")
    else:
        print("\n[CONCLUSION] Bundle Verification FAILED.")
        sys.exit(1)

if __name__ == "__main__":
    verify_bundle()
