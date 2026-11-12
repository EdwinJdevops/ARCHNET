#!/usr/bin/env bash
set -euo pipefail

[[ $(kind version) == "kind v0.30.0 "* ]]
work_dir=$(mktemp -d)
cluster="archnet-$(basename "$work_dir" | tr '[:upper:]' '[:lower:]' | tr -cd '[:alnum:]')"
export KUBECONFIG="$work_dir/kubeconfig"
export KIND_EXPERIMENTAL_PROVIDER=docker
cleanup() {
  local status=$?
  trap - EXIT
  kind delete cluster --name "$cluster" || status=1
  rm -rf -- "$work_dir"
  exit "$status"
}
trap cleanup EXIT

kind create cluster --name "$cluster" --wait 180s \
  --image kindest/node:v1.34.0@sha256:7416a61b42b1662ca6ca89f02028ac133a309a2a30ba309614e8ec94d976dc5a

kubectl() {
  docker exec "$cluster-control-plane" kubectl --kubeconfig=/etc/kubernetes/admin.conf "$@"
}
kubectl wait --for=condition=Ready node --all --timeout=120s
kubectl rollout status deployment/coredns -n kube-system --timeout=120s
kubectl create namespace archnet-smoke
kubectl -n archnet-smoke create configmap smoke --from-literal=ready=true
[[ $(kubectl -n archnet-smoke get configmap smoke -o 'jsonpath={.data.ready}') == true ]]
