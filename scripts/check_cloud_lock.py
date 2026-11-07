#!/usr/bin/env python3
"""Verify the explicit cloud deployment safety lock has not been removed.

Static defense-in-depth only: does not evaluate Terraform expressions or plans.
"""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1] / "terraform"
variables = (root / "variables.tf").read_text(encoding="utf-8")
main = (root / "main.tf").read_text(encoding="utf-8")
checks = {
    "cloud deployment variable defaults false":
        bool(re.search(r'variable\s+"enable_cloud_deployment"\s*\{[^{}]*\bdefault\s*=\s*false', variables, re.S)),
    "cloud deployment variable has deny-true validation":
        bool(re.search(r'condition\s*=\s*var\.enable_cloud_deployment\s*==\s*false', variables)),
    "EC2 resource is controlled by cloud deployment variable":
        bool(re.search(r'resource\s+"aws_instance"\s+"k3s"\s*\{\s*count\s*=\s*var\.enable_cloud_deployment\s*\?\s*1\s*:\s*0', main)),
}
for label, ok in checks.items():
    print(("PASS" if ok else "FAIL") + ": " + label)
sys.exit(0 if all(checks.values()) else 1)
