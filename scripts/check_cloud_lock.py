#!/usr/bin/env python3
"""Reject any executable Terraform configuration beyond the reviewed empty root."""
from pathlib import Path
import sys

repo = Path(__file__).resolve().parents[1]
expected = {
    "terraform/main.tf": "terraform {\n  required_version = \"= 1.12.2\"\n}\n",
    "terraform/variables.tf": "variable \"enable_cloud_deployment\" {\n  description = \"Cloud provisioning is disabled.\"\n  type        = bool\n  default     = false\n  nullable    = false\n\n  validation {\n    condition     = var.enable_cloud_deployment == false\n    error_message = \"Cloud deployment is intentionally disabled.\"\n  }\n}\n",
}
actual = {
    path.relative_to(repo).as_posix()
    for path in repo.rglob("*")
    if path.name.endswith((".tf", ".tf.json"))
}
if actual != expected.keys():
    sys.exit(f"Unexpected Terraform source inventory: {sorted(actual)}")
for name, source in expected.items():
    path = repo / name
    if path.is_symlink() or path.read_text(encoding="utf-8") != source:
        sys.exit(f"Terraform source differs from the reviewed cloud-disabled root: {name}")
print("PASS: provider-free Terraform source and deny-true lock")
