# ARCHNET

Experimental repository for reviewing a cloud-disabled infrastructure baseline in pull requests. CI checks whether the Terraform root proposes zero changes without cloud credentials and rejects an attempt to enable provisioning. A disposable kind cluster checks local Kubernetes API readiness and object reconciliation prerequisites.

- [Reproduce the cloud-disabled Terraform benchmark](docs/CLOUD_LOCK_BENCHMARK.md)
- [Architecture, demand evidence and alternatives](docs/ENGINEERING_AUDIT.md)
- [Cost boundary and local Kubernetes instructions](docs/DEPLOYMENT_SAFETY.md)

The Argo CD Application is reference configuration. The Kubernetes smoke test does not deploy it, validate application workloads or demonstrate production readiness.

## Quickstart

From a fresh checkout on Linux or WSL with Python 3, Bash, Terraform 1.12.2 and jq:

```sh
python scripts/benchmark_cloud_lock.py
bash scripts/verify_cloud_plan.sh
```

Expect the clean source and zero-change plan to pass, both source regressions to be rejected, and explicit cloud enablement to fail with the disabled-cloud diagnostic. To adapt IAM testing to your own module, start with the [two-module workflow](.github/workflows/full-module-iam.yml). That workflow tests a targeted plan without AWS network access after dependency setup.

See [LICENSE](LICENSE), [third-party notices](THIRD_PARTY_NOTICES.md), and [maintainer contact](MAINTAINERS.md).
