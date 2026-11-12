"""Run the real source guard against an isolated copy of the approved root."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

REPO = Path(__file__).resolve().parents[1]
GUARD = Path("scripts/check_cloud_lock.py")
FIXTURE = REPO / "tests/fixtures/unexpected-resource.tf.fixture"


def check(root, case, expected_code, expected_message):
    started = time.perf_counter()
    result = subprocess.run(
        [sys.executable, str(root / GUARD)],
        capture_output=True,
        text=True,
        timeout=10,
    )
    elapsed = time.perf_counter() - started
    output = result.stdout + result.stderr
    print(f"{case}: exit={result.returncode}, elapsed={elapsed:.3f}s", flush=True)
    print(output, end="", flush=True)
    if result.returncode != expected_code or expected_message not in output:
        raise SystemExit(f"Unexpected policy decision for {case}")


def main():
    with tempfile.TemporaryDirectory(prefix="archnet-policy-") as directory:
        root = Path(directory)
        (root / GUARD.parent).mkdir()
        shutil.copyfile(REPO / GUARD, root / GUARD)
        (root / "terraform").mkdir()
        for name in ("main.tf", "variables.tf"):
            relative = Path("terraform") / name
            shutil.copyfile(REPO / relative, root / relative)
        check(root, "clean source", 0, "PASS: provider-free Terraform source")
        shutil.copyfile(FIXTURE, root / "terraform/unexpected.tf")
        check(
            root,
            "unexpected declaration",
            1,
            "Unexpected Terraform source inventory: ['terraform/main.tf', "
            "'terraform/unexpected.tf', 'terraform/variables.tf']",
        )


if __name__ == "__main__":
    main()
