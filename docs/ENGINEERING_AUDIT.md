# ARCHNET engineering audit

## Candidate workflow

A platform engineer reviewing changes to an intentionally cloud-disabled sandbox needs commit-specific proof that the disabled Terraform root still proposes zero changes, without granting the pull request cloud credentials. Limit this experiment to the zero-change contract and a disposable local Kubernetes check. The original repo combined AWS scaffolding, a reference Argo CD Application and static CI. At the audited revision, the false flag suppressed EC2 while six networking resources remained unconditional and an AMI data source could still query AWS. Argo CD pointed at the apps directory on main with manual sync. The repository provides no verified bootstrap, recovery or operator handoff.

## Evidence and alternatives

- [Atlantis issue #3297](https://github.com/runatlantis/atlantis/issues/3297) records a request to isolate plan from apply and the maintenance burden of provider allowlists. [Atlantis security documentation](https://www.runatlantis.io/docs/security.html) explains why planning pull-request code with infrastructure credentials creates a trust boundary. [Issue #2144](https://github.com/runatlantis/atlantis/issues/2144) describes separate Terraform project scopes and credentials. These are examples of plan execution and credential scoping friction. They do not demonstrate demand for ARCHNET or establish how often teams need this specific zero-change check. A repository issue search returned no ARCHNET issues.
- [Terraform provider mocks](https://developer.hashicorp.com/terraform/language/tests/mocking) suit testing modules with provider resources and data sources when real credentials are unavailable. Here the root intentionally contains no providers or resources, so a real empty plan directly tests the narrower invariant.
- [Conftest](https://open-policy-agent.github.io/conftest/) can evaluate JSON with reusable policy across repositories. A small plan predicate is enough for this one invariant. Atlantis suits teams that need a coordinated plan/apply workflow and can operate the required trust boundaries. [kind](https://kind.sigs.k8s.io/docs/user/quick-start/) supplies the local cluster directly.

Before expanding scope, ask independent platform engineers for recent examples, how often the review repeats, how they verify it today, and whether they would adopt this check instead of their existing CI. Test one real sandbox PR with a second operator and record time to a reviewable result and any missed regressions. Adoption, savings and differentiation remain unvalidated.

## Verification baseline

[Run #19](https://github.com/EdwinJdevops/ARCHNET/actions/runs/42384163801) passed validation, Terraform formatting/configuration and Trivy on [the audited commit](https://github.com/EdwinJdevops/ARCHNET/commit/b260163d4861a2f476d35707c024079bf7ecf026). That run did not execute a Terraform plan or start a cluster. Review the checks on the current PR head for the new gates.
