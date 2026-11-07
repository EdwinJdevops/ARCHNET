# ARCHNET — Internal Developer Platform research

**Status: experimental / not production-ready.** This repository is undergoing a source, deployment and operational safety audit. No customer production use is authorized or validated.

## Current scope

The repository contains Terraform for an AWS VPC and EC2 instance, an Argo CD Application reference, and CI checks. The original README described additional security, observability and automation features that have **not been independently verified** in this audit. Do not interpret the architecture as an operational deployment.

## Deployment safety

**Cloud instance creation is disabled by default and explicitly locked.** The earlier bootstrap script referenced by Terraform was missing; it has not been replaced with an unreviewed remote installer. The default instance size was `t3.medium` and must not be provisioned without a complete cost assessment.

Do not run `terraform apply` expecting a functioning k3s cluster. The current infrastructure does not implement a secure administrative access path or a validated cluster bootstrap.

See [deployment safety](docs/DEPLOYMENT_SAFETY.md).

## Continuous integration

The CI workflow parses YAML, checks shell syntax and required directories, rejects known public SSH/Kubernetes API ingress rules, and runs a critical-severity filesystem scan. These are limited static checks, not evidence of a working deployment.

## Planned operator acceptance criteria

1. A second engineer can install and recover a disposable environment from written instructions.
2. Access controls, secrets and dependency provenance are reviewed.
3. Backups are restored successfully under test.
4. Release and rollback paths are reproducible.
5. Reliability objectives and chaos-test results are measured and published.
6. No cloud costs are incurred without a documented estimate and authorization.

## Contributing

Submit a narrowly scoped issue or pull request with reproducible steps, tests, observed behavior and security implications. Do not post secrets or real customer data. Proposed production claims require independently verifiable evidence.
