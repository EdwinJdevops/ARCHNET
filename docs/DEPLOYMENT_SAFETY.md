# Deployment safety and cost boundary

The infrastructure ceiling is **$10/month**. This baseline authorizes **$0 in live cloud spend**. There are no executable AWS resources, AWS provider, remote backend, AMI reads or deployment steps in the Terraform root. The previous AWS design is available in [the audited revision](https://github.com/EdwinJdevops/ARCHNET/tree/b260163d4861a2f476d35707c024079bf7ecf026/terraform). The empty-root test uses fresh checkout state. Anyone who has previously applied the old root should keep that state separate and review it independently before running Terraform against it.

CI checks the Terraform source inventory before initialization, requires a no-change saved plan and inspects its JSON for resources, drift, outputs, providers and module calls. Setting `enable_cloud_deployment=true` must fail with the specific validation diagnostic. The earlier literal ingress checker remains covered by its unit tests and is scoped to the retired AWS design. Repository checks can be edited in a PR, so any future enforced merge rule needs trusted review of workflow and policy changes.

## Disposable Kubernetes smoke test

On Linux or WSL with a working Linux Docker engine, Bash and Go, run from the repository root:

```sh
go install sigs.k8s.io/kind@v0.30.0
export PATH="$(go env GOPATH)/bin:$PATH"
bash scripts/smoke_kind.sh
```

With a custom GOBIN, add that directory to PATH instead. The script uses a digest-pinned Kubernetes node image, a unique cluster name and a temporary kubeconfig. It checks node readiness, CoreDNS rollout and a ConfigMap round trip. It attempts cluster teardown on exit and fails if teardown fails. The test uses public dependency downloads and local compute. It covers neither Argo CD nor workload deployment, DNS queries, recovery or production operations.

Any future AWS proposal needs separate authorization, a reviewed bootstrap and admin access path, and a full cost estimate covering compute, storage, public IPs, data transfer, monitoring, snapshots and tax. Billing alerts do not cap spending.
