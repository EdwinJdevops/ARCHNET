#!/usr/bin/env bash
set -euo pipefail

root=$(mktemp -d)
trap 'rm -rf -- "$root"' EXIT
terraform_bin=$(command -v terraform)
for module in eks cloudposse; do
  mkdir "$root/$module"
  cp "tests/fixtures/iam/$module.tf.fixture" "$root/$module/main.tf"
  (
    cd "$root/$module"
    CHECKPOINT_DISABLE=1 terraform init -backend=false -input=false
  )
done

render() {
  sudo unshare --net -- env -i PATH=/usr/bin:/bin CHECKPOINT_DISABLE=1 \
    AWS_EC2_METADATA_DISABLED=true "$terraform_bin" -chdir="$1" \
    plan -input=false -refresh=false -no-color -out="$1/result.plan"
  "$terraform_bin" -chdir="$1" show -json "$1/result.plan" |
    jq -e --argjson expected "$2" '.planned_values.outputs.principal_matches.value == $expected'
}

for module in eks cloudposse; do
  dir="$root/$module"
  echo "$module: original principal must match"
  render "$dir" true
  if [[ "$module" == eks ]]; then
    sed -i 's/identifiers = \["eks.amazonaws.com"\]/identifiers = ["ec2.amazonaws.com"]/' "$dir/main.tf"
  else
    sed -i '/aws_account_number *=/s/111122223333/444455556666/' "$dir/main.tf"
  fi
  echo "$module: changed principal must fail the same assertion"
  render "$dir" false
done
