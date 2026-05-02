# Archnet: Zero-Trust Internal Developer Platform

A production-grade Internal Developer Platform built with k3s, ArgoCD, and observability-first architecture.

## Architecture
GitHub Repo → GitHub Actions → Docker Registry → ArgoCD → k3s Cluster → Prometheus + Grafana

## Tech Stack
- Kubernetes: k3s
- GitOps: ArgoCD
- Secrets: Sealed-Secrets
- Monitoring: Prometheus + Grafana
- Logging: Loki
- CI/CD: GitHub Actions
- IaC: Terraform

## Features
- Fully declarative GitOps deployments
- Automated secret rotation
- Self-healing via ArgoCD drift detection
- Production-grade observability
- RBAC audit logging
- Zero-trust network policies

## Quick Start
1. Clone repo
2. cd terraform && terraform init && terraform apply
3. kubectl port-forward svc/argocd-server -n argocd 8080:443
4. Access Grafana at localhost:3000

## Project Structure
- terraform/ - AWS infrastructure
- k3s/ - Cluster setup
- argocd/ - GitOps manifests
- observability/ - Prometheus, Grafana, Loki
- apps/ - Application deployments
- docs/ - Technical documentation

## Built by Edwin | DevOps Engineer | Nigeria
