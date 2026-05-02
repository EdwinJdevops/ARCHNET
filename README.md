# Archnet: Zero-Trust Internal Developer Platform

![CI/CD](https://github.com/EdwinJdevops/ARCHNET/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue)
![Stack](https://img.shields.io/badge/stack-k3s%20%7C%20ArgoCD%20%7C%20Prometheus-brightgreen)

> A production-grade Internal Developer Platform built by a self-taught DevOps Engineer from Nigeria.

## Problem It Solves
Most teams deploy to Kubernetes manually — no automation, no observability, no drift detection. Archnet automates the entire platform lifecycle.

## Architecture
Developer → Git Push
→ GitHub Actions (CI)
→ Docker Registry
→ ArgoCD (GitOps)
→ k3s Cluster
→ Prometheus + Grafana
→ AlertManager → Slack

## Tech Stack
| Tool | Purpose |
|------|---------|
| k3s | Lightweight production Kubernetes |
| ArgoCD | GitOps deployments + drift detection |
| Sealed-Secrets | Zero-trust secret management |
| Prometheus | Metrics collection |
| Grafana | Dashboards + alerting |
| Loki | Log aggregation |
| GitHub Actions | CI/CD pipeline |
| Terraform | AWS infrastructure as code |

## Key Features
- Self-healing deployments (ArgoCD drift detection)
- Secrets encrypted at rest in Git
- Full observability stack (metrics + logs + alerts)
- RBAC audit logging
- Zero-trust network policies
- Single-command infrastructure provisioning

## Quick Start
```bash
# 1. Clone
git clone https://github.com/EdwinJdevops/ARCHNET
cd ARCHNET

# 2. Provision AWS infrastructure
cd terraform
terraform init
terraform plan
terraform apply

# 3. Access ArgoCD
kubectl port-forward svc/argocd-server -n argocd 8080:443

# 4. Access Grafana
kubectl port-forward svc/grafana -n monitoring 3000:3000
```

## Project Structure
archnet/
├── .github/workflows/    # CI/CD pipeline
├── terraform/            # AWS infrastructure
├── k3s/                  # Cluster setup
├── argocd/               # GitOps manifests
├── observability/        # Prometheus, Grafana, Loki
├── apps/                 # Application deployments
└── docs/                 # Architecture + decisions

## Security Model
- Default deny network policies
- RBAC least-privilege access
- Sealed-Secrets (decrypt only inside cluster)
- Trivy image scanning pre-deploy
- No secrets in environment variables

## Documentation
- [Architecture](docs/ARCHITECTURE.md)
- [Tech Decisions](docs/TECH_DECISIONS.md)
- [Security](docs/SECURITY.md)

## Author
**Edwin** | DevOps & Cloud Engineer | Nigeria
[LinkedIn](https://linkedin.com/in/YOUR_LINKEDIN) · [Hashnode](https://YOUR_HASHNODE.hashnode.dev)

---
> Built to solve real infrastructure problems. Not a tutorial project.
