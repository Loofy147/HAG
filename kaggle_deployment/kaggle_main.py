import os
import subprocess
import sys
import time
import shutil
from datetime import datetime

def run_command(command, description):
    print(f"\n{'='*20} {description} {'='*20}")
    start_time = time.time()
    try:
        # Using shell=True to support piping and multi-commands
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {description}:")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
    end_time = time.time()
    print(f"Duration: {end_time - start_time:.2f} seconds")

def main():
    print(f"HAG-Desktop Build 4.0 Kaggle Execution Engine")
    print(f"Started at: {datetime.now().isoformat()}")

    # 1. Environment Setup (Kaggle specific)
    # Check if we are running in /kaggle/working
    working_dir = "/kaggle/working"
    input_dir = "/kaggle/input/hag-desktop-v4"

    if os.path.exists(input_dir):
        print(f"Detected Kaggle Input Dataset at {input_dir}")
        # Copy files to working directory if they aren't already there
        # This allows editable installs and execution of scripts
        for item in os.listdir(input_dir):
            s = os.path.join(input_dir, item)
            d = os.path.join(working_dir, item)
            if os.path.isdir(s):
                if os.path.exists(d): shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)

    os.chdir(working_dir)
    print(f"Current Working Directory: {os.getcwd()}")

    # 2. Dependencies
    run_command("pip install -r requirements.txt", "Installing Dependencies")
    run_command("pip install .", "Installing HAG Package")

    # 3. System Verification
    run_command("python3 scripts/sovereignty_master_proof.py", "Running Sovereignty Master Proof")

    # 4. Stress Testing
    run_command("python3 scripts/full_system_stress_test.py", "Running Full System Stress Test")

    # 5. Manifold Stability (GPU Test)
    run_command("python3 scripts/manifold_stability_test.py", "Running Manifold Stability Test")

    # 6. CLI Check
    run_command("hag-cli --version", "Verifying HAG-CLI")

    print(f"\nExecution Finished at: {datetime.now().isoformat()}")

if __name__ == "__main__":
    main()
