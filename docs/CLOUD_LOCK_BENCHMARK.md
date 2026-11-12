# Cloud-disabled Terraform benchmark

Run from the repository root on Linux or WSL with Python 3, Bash, Terraform 1.12.2 and jq.

```sh
python scripts/benchmark_cloud_lock.py
bash scripts/verify_cloud_plan.sh
```

Use a fresh checkout without existing Terraform state. These are the same commands CI runs. The source benchmark copies the checked-in root and policy into a temporary directory and uses the same provider-free `terraform_data` fixture in two isolated regression cases. It first adds an unexpected file, then removes that file and appends the declaration to the approved `main.tf`. It never invokes Terraform and leaves the checkout untouched. The real plan script checks the live source inventory before initializing Terraform.

| Case | Expected evidence |
| --- | --- |
| Clean source | Source guard exits 0. |
| Unexpected declaration | Source guard exits 1 and names the added file. |
| Declaration appended to approved file | Source guard exits 1 and identifies the modified `terraform/main.tf`. |
| Disabled Terraform root | Terraform exits 0 with zero changes, and the plan JSON policy passes. |
| Explicit enablement | Terraform rejects the input with the cloud-disabled diagnostic. |

The job fails if any decision differs. Logs report elapsed time for each source check and each Terraform plan command. Source timings include Python process startup. Timings describe that run and exclude queue time and setup. View the Terraform job in the [workflow history](https://github.com/EdwinJdevops/ARCHNET/actions/workflows/ci.yml) for the commit under review. Kubernetes smoke results appear in a separate job.

This benchmark verifies the disabled-root contract and two representative source regressions. It provides no evidence about adoption, production operation or the performance of a live AWS plan.
