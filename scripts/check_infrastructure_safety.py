#!/usr/bin/env python3
"""Fail-closed checks for known dangerous ARCHNET infrastructure defaults."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TERRAFORM = ROOT / "terraform" / "main.tf"

def check():
    failures = []
    if not TERRAFORM.is_file():
        return ["Missing terraform/main.tf"]
    source = TERRAFORM.read_text(encoding="utf-8")
    # Inspect ingress blocks, not egress rules. This is a conservative guard,
    # not a complete Terraform parser or a replacement for plan/policy checks.
    ingress_blocks = re.findall(r"\bingress\s*\{([^{}]*)\}", source, re.S)
    if not ingress_blocks:
        failures.append("No ingress blocks found; review Terraform manually")
    for block in ingress_blocks:
        if re.search(r'cidr_blocks\s*=\s*\[\s*"0\.0\.0\.0/0"\s*\]', block):
            ports = re.findall(r'(?:from_port|to_port)\s*=\s*(\d+)', block)
            if any(p in {"22", "6443"} for p in ports):
                failures.append("Public SSH or Kubernetes API ingress detected")
    return failures

if __name__ == "__main__":
    errors = check()
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    if errors:
        sys.exit(1)
    print("Known public control-plane ingress checks passed")
