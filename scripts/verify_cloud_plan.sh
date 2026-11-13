#!/usr/bin/env bash
set -euo pipefail

repo_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
python "$repo_dir/scripts/check_cloud_lock.py"
cd -- "$repo_dir/terraform"
export CHECKPOINT_DISABLE=1 AWS_EC2_METADATA_DISABLED=true
terraform init -backend=false -input=false
terraform fmt -check -recursive -diff
terraform validate -no-color

TIMEFORMAT='Elapsed: %3R s'
plan_dir=$(mktemp -d)
trap 'rm -rf -- "$plan_dir"' EXIT
echo 'CASE: disabled baseline must produce zero changes'
time terraform plan -input=false -refresh=false -detailed-exitcode -out="$plan_dir/disabled.tfplan"
terraform show -json "$plan_dir/disabled.tfplan" | jq -e '
  .format_version == "1.2" and .errored == false and
  .variables.enable_cloud_deployment.value == false and
  ((.resource_changes // []) | length == 0) and
  ((.resource_drift // []) | length == 0) and
  ((.output_changes // {}) | length == 0) and
  ((.configuration.provider_config // {}) | length == 0) and
  ((.configuration.root_module.resources // []) | length == 0) and
  ((.configuration.root_module.module_calls // {}) | length == 0)
'
echo 'CASE: explicit enablement must be rejected'
if time terraform plan -input=false -refresh=false -no-color -var=enable_cloud_deployment=true >"$plan_dir/denied.log" 2>&1; then
  echo "Cloud enablement unexpectedly passed" >&2
  exit 1
fi
cat "$plan_dir/denied.log"
grep -F 'Cloud deployment is intentionally disabled.' "$plan_dir/denied.log"
