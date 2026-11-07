# Deployment safety and cost boundary

Status: **not validated for production use**. Do not apply the current Terraform to customer infrastructure.

## Immediate security controls

The initial AWS configuration exposed SSH (22/TCP) and the Kubernetes API
(6443/TCP) to the public internet. This branch removes both ingress rules.
The cluster must not be assumed remotely manageable after this change.
A separate, authenticated administrative access design and recovery procedure
must be reviewed before deployment.

The existing public HTTP and HTTPS ingress rules also require an application
threat model, TLS configuration and verification before deployment.

The static guard in `scripts/check_infrastructure_safety.py` detects only
simple literal Terraform ingress blocks. It is not a complete security
policy engine and does not analyze modules, dynamic expressions or actual
cloud state. Review `terraform plan` and cloud permissions independently.

## Budget: maximum $10/month

Default: no continuously running cloud infrastructure. Use local disposable
environments and short-lived CI tests. Never provision AWS resources without
an independently checked estimate including compute, EBS, IPv4, data transfer,
monitoring, snapshots and tax. Use account budgets and alerts; alerts are not
hard spending limits.

No chaos experiments against customer infrastructure. Tests must be isolated,
authorized, bounded, and followed by recovery verification.

## Required before any production-readiness claim

- Verified installation from a clean environment by a second operator
- Locked and reviewed dependency versions and supply-chain scanning
- Working deployment, rollback and disaster recovery runbooks
- Access control and secret management review
- Measured backup restoration, SLOs and failure behavior
- Reviewed Terraform plan and complete cost estimate
- Passing CI on the exact commit being released

A successful static check or CI run does not establish production readiness.
