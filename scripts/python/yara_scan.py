#This is a malicious file scanner

import yara
import os

RULES_DIR = "rules"
TARGET_DIR = "files_to_scan"

def load_rules():
    rule_files = {f: os.path.join(RULES_DIR, f) for f in os.listdir(RULES_DIR) if f.endswith(".yar")}
    return yara.compile(filepaths=rule_files)

def scan_files(rules):
    for file in os.listdir(TARGET_DIR):
        file_path = os.path.join(TARGET_DIR, file)
        matches = rules.match(file_path)
        if matches:
            print(f"ALERT: {file} matches YARA rule {matches}")

if __name__ == "__main__":
    yara_rules = load_rules()
    scan_files(yara_rules)

