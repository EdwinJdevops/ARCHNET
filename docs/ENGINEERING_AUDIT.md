# ARCHNET engineering audit

## Candidate workflow

A platform engineer reviewing changes to an intentionally cloud-disabled sandbox needs commit-specific proof that the disabled Terraform root still proposes zero changes, without granting the pull request cloud credentials. Limit this experiment to the zero-change contract and a disposable local Kubernetes check. The original repo combined AWS scaffolding, a reference Argo CD Application and static CI. At the audited revision, the false flag suppressed EC2 while six networking resources remained unconditional and an AMI data source could still query AWS. Argo CD pointed at the apps directory on main with manual sync. The repository provides no verified bootstrap, recovery or operator handoff.

## Evidence and alternatives

- [Atlantis issue #3297](https://github.com/runatlantis/atlantis/issues/3297) records a request to isolate plan from apply and the maintenance burden of provider allowlists. [Atlantis security documentation](https://www.runatlantis.io/docs/security.html) explains why planning pull-request code with infrastructure credentials creates a trust boundary. [Issue #2144](https://github.com/runatlantis/atlantis/issues/2144) describes separate Terraform project scopes and credentials. These are examples of plan execution and credential scoping friction. They do not demonstrate demand for ARCHNET or establish how often teams need this specific zero-change check. A repository issue search returned no ARCHNET issues.
- [Terraform provider mocks](https://developer.hashicorp.com/terraform/language/tests/mocking) suit testing modules with provider resources and data sources when real credentials are unavailable. Here the root intentionally contains no providers or resources, so a real empty plan directly tests the narrower invariant.
- [Conftest](https://open-policy-agent.github.io/conftest/) can evaluate JSON with reusable policy across repositories. A small plan predicate is enough for this one invariant. Atlantis suits teams that need a coordinated plan/apply workflow and can operate the required trust boundaries. [kind](https://kind.sigs.k8s.io/docs/user/quick-start/) supplies the local cluster directly.

The [reproducible benchmark](CLOUD_LOCK_BENCHMARK.md) lets a solo maintainer publish review evidence for clean and regressed configurations. Before expanding scope, look for concrete reports from unrelated teams and record their existing safeguards and unresolved gaps. Adoption, savings and differentiation remain unvalidated.

## Public evidence review

| Source | Observed friction | Scope of the evidence |
| --- | --- | --- |
| [Atlantis #3297](https://github.com/runatlantis/atlantis/issues/3297) | A requester wanted isolated planning and reported maintenance cost for provider allowlists. | Supports plan isolation as a concern. The reported workflow includes live infrastructure. |
| [AWS provider #29141](https://github.com/hashicorp/terraform-provider-aws/issues/29141) | A plan failed to resolve credentials from the configured file. The reporter used an environment variable as a workaround. | A concrete credential failure. No cloud-disabled PR workflow is described. |
| [Terraform #17034](https://github.com/hashicorp/terraform/issues/17034) | Terraform maintainers describe why plan can read external data even when implicit refresh is disabled. | Explains the mechanism that made ARCHNET's AMI declaration relevant. It is a design record. |
| [Terragrunt authentication](https://docs.terragrunt.com/features/units/authentication/) | Documents separate read-only plan and read-write apply roles. | A practical alternative when a plan must read live infrastructure. |

The public record corroborates credential and planning friction. The repository audit is the only directly observed example in this review of a cloud-disabled root that still declared live AWS dependencies. Keep the benchmark as a reusable engineering baseline. Expand the product only when another concrete case identifies the same contract and an unmet need.

## Merge verification

The four checks run on the draft PR. Active required-check enforcement on `main` could not be verified from available repository rules access. A green run confirms execution for the tested revision. Before a future merge, inspect the active rule for `main` and confirm it requires the expected checks and protects changes to the workflow and policy. The PR remains draft.

## Verification baseline

[Run #19](https://github.com/EdwinJdevops/ARCHNET/actions/runs/42384163801) passed validation, Terraform formatting/configuration and Trivy on [the audited commit](https://github.com/EdwinJdevops/ARCHNET/commit/b260163d4861a2f476d35707c024079bf7ecf026). That run did not execute a Terraform plan or start a cluster. Review the checks on the current PR head for the new gates.
