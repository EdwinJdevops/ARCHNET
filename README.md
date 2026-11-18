# ARCHNET

![ARCHNET logo](docs/assets/archnet.png)

**Catch Terraform regressions before handing CI cloud credentials.**

ARCHNET is an Apache-2.0 preview for platform engineers maintaining cloud-disabled Terraform roots or testing generated IAM policies. Start with one of two workflows.

| What you need to verify | Start here |
| --- | --- |
| A cloud-disabled root still plans zero changes | Run the quickstart below. It checks the plan and exercises two source regressions. |
| A generated IAM policy still contains the intended permission | Adapt the [UK Trade workflow](.github/workflows/uktrade-iam.yml). It tests the real rendered policy from the upstream module root. |

## Quickstart

From a fresh checkout on Linux or WSL with Python 3, Bash, Terraform 1.12.2, and jq:

```sh
python scripts/benchmark_cloud_lock.py
bash scripts/verify_cloud_plan.sh
```

Expect a zero-change plan, rejection of an added Terraform file and an in-place resource declaration, and the expected failure when cloud deployment is explicitly enabled. The source guard is specific to ARCHNET’s two approved files. See the [benchmark and expected output](docs/CLOUD_LOCK_BENCHMARK.md).

## Test the generated IAM policy

A mock can return valid JSON even when the policy source regresses. In the pinned UK Trade module, CI rendered the actual policy and rejected a mutation that replaced `iam:CreateRole` with `iam:GetUser`. The workflow installs dependencies first, then runs a targeted Terraform plan with networking disabled and no real AWS credentials. [Upstream test workaround](https://github.com/uktrade/terraform-platform-modules/pull/189/files) · [Verified CI result](https://github.com/EdwinJdevops/ARCHNET/actions/runs/44298893164/job/134783065448)

Use the [EKS and Cloud Posse examples](.github/workflows/full-module-iam.yml) for trust principals. These recipes use native Terraform. The experiments establish regression detection for the tested policies. Setup savings, full untargeted plans, and production behavior remain unverified.

[Deployment safety and local Kubernetes](docs/DEPLOYMENT_SAFETY.md) · [Engineering audit](docs/ENGINEERING_AUDIT.md) · [Maintainer contact](MAINTAINERS.md) · [Apache 2.0](LICENSE) · [Third-party notices](THIRD_PARTY_NOTICES.md)
