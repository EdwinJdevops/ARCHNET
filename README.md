# ARCHNET

Experimental repository for reviewing a cloud-disabled infrastructure baseline in pull requests. CI checks whether the Terraform root proposes zero changes without cloud credentials and rejects an attempt to enable provisioning. A disposable kind cluster checks local Kubernetes API readiness and object reconciliation prerequisites.

- [Reproduce the cloud-disabled Terraform benchmark](docs/CLOUD_LOCK_BENCHMARK.md)
- [Architecture, demand evidence and alternatives](docs/ENGINEERING_AUDIT.md)
- [Cost boundary and local Kubernetes instructions](docs/DEPLOYMENT_SAFETY.md)

The Argo CD Application is reference configuration. The Kubernetes smoke test does not deploy it, validate application workloads or demonstrate production readiness.
