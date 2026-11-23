# Kubernetes reference manifest

The previous demo workload used a mutable image tag and had no runtime acceptance test. Use the disposable control-plane smoke test in scripts/smoke_kind.sh. Add a workload only with a digest-pinned image and verified runtime checks.
