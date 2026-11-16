#!/usr/bin/env python3
"""Conservative guard for simple inline Terraform ingress declarations.

This is not a complete HCL parser or a substitute for plan-time policy.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TERRAFORM = ROOT / "terraform" / "main.tf"

def check_source(source: str) -> list[str]:
    errors = []
    blocks = re.findall(r"\bingress\s*\{([^{}]*)\}", source, re.S)
    if not blocks:
        return ["No inline ingress blocks found; manual policy review required"]
    for block in blocks:
        if not re.search(r'\b(?:cidr_blocks)\s*=\s*\[[^\]]*"0\.0\.0\.0/0"[^\]]*\]', block, re.S):
            continue
        start = re.search(r"\bfrom_port\s*=\s*(\d+)", block)
        end = re.search(r"\bto_port\s*=\s*(\d+)", block)
        protocol = re.search(r'\bprotocol\s*=\s*"([^"]+)"', block)
        if not start or not end or not protocol:
            errors.append("Unresolved public ingress rule; manual review required")
            continue
        lo, hi = int(start.group(1)), int(end.group(1))
        if protocol.group(1).lower() in {"tcp", "6", "-1"} and (lo <= 22 <= hi or lo <= 6443 <= hi or protocol.group(1) == "-1"):
            errors.append("Public SSH or Kubernetes API ingress detected")
    return errors

def check() -> list[str]:
    if not TERRAFORM.is_file():
        return ["Missing terraform/main.tf"]
    return check_source(TERRAFORM.read_text(encoding="utf-8"))

if __name__ == "__main__":
    errors = check()
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    sys.exit(1 if errors else 0)
