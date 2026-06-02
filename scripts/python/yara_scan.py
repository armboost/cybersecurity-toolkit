#This is a malicious file scanner

import yara
import os
import sys

RULES_DIR = "rules"
TARGET_DIR = "files_to_scan"

def load_rules():
    """Load YARA rules from the rules directory."""
    if not os.path.exists(RULES_DIR):
        print(f"Warning: Rules directory '{RULES_DIR}' not found. Creating it...")
        os.makedirs(RULES_DIR, exist_ok=True)
        print("No YARA rules to compile. Skipping scan.")
        return None
    
    rule_files = [f for f in os.listdir(RULES_DIR) if f.endswith(".yar")]
    
    if not rule_files:
        print(f"Warning: No .yar files found in '{RULES_DIR}'. Skipping scan.")
        return None
    
    file_paths = {f: os.path.join(RULES_DIR, f) for f in rule_files}
    try:
        return yara.compile(filepaths=file_paths)
    except yara.Error as e:
        print(f"Error compiling YARA rules: {e}")
        return None

def scan_files(rules):
    """Scan files in TARGET_DIR against the compiled YARA rules."""
    if rules is None:
        print("No rules available. Skipping file scan.")
        return
    
    if not os.path.exists(TARGET_DIR):
        print(f"Warning: Target directory '{TARGET_DIR}' not found. Creating it...")
        os.makedirs(TARGET_DIR, exist_ok=True)
        return
    
    files = os.listdir(TARGET_DIR)
    if not files:
        print(f"No files found in '{TARGET_DIR}' to scan.")
        return
    
    for file in files:
        file_path = os.path.join(TARGET_DIR, file)
        if os.path.isfile(file_path):
            try:
                matches = rules.match(file_path)
                if matches:
                    print(f"ALERT: {file} matches YARA rule: {matches}")
                else:
                    print(f"OK: {file} passed YARA scan")
            except yara.Error as e:
                print(f"Error scanning {file}: {e}")

if __name__ == "__main__":
    yara_rules = load_rules()
    scan_files(yara_rules)
    print("YARA scan completed successfully!")
