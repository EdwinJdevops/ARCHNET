# CNCF readiness review

Reviewed 27 November 2026 against the CNCF Sandbox application.

| Requirement | Evidence and state |
| --- | --- |
| Apache 2.0 project license | LICENSE is present and recognized by GitHub. |
| Repository age | Created 30 April 2026, older than six months. |
| Maintainer identity | MAINTAINERS.md lists name, GitHub ID, affiliation and contact. Affiliation is self-reported on GitHub. |
| Reusable project eligibility | Open. Current deliverable is a benchmark and native Terraform testing recipes. No independent adoption or advantage over a small native test has been demonstrated. |
| Dependency licensing | Open. Terraform CLI is BSL. Its role as an external test tool must be disclosed and assessed under CNCF policy. Transitive tool dependencies have not received a complete license inventory. |
| Security | Private reporting enabled. CI scans HIGH/CRITICAL findings. A full security audit remains open. |
| Contribution process | CONTRIBUTING.md is present. |
| Code of conduct | CODE_OF_CONDUCT.md defines conduct, private reporting and enforcement, including the one-maintainer appeals limitation. |
| Trademark and contribution agreement | Open. No trademark clearance or signed foundation contribution agreement is claimed. |

Application contact is Edwin Jonathan, Nigeria, edwinjonathanchibuike123@gmail.com. A foundation agreement needs the individual's own signature.

Sources: [Sandbox application](https://github.com/cncf/sandbox/blob/main/.github/ISSUE_TEMPLATE/application.yml), [criteria](https://github.com/cncf/sandbox/blob/main/README.md).

Do not describe ARCHNET as accepted, donated or foundation-managed. Submission readiness remains incomplete until the open eligibility and licensing questions are resolved.

## Operational acceptance gates

The supported execution surface is disposable CI and local test recipes. All eight demonstrated PR check contexts are required by main branch protection. Test runner network isolation and synthetic credentials prevent the tested IAM plans from contacting AWS after setup.

A hosted production service has no implemented deployment, authenticated user interface, tenancy model, service monitoring, backup or recovery path in this repository. Define a specific service and its users before implementing those components. The current CLI recipes have not received independent onboarding measurements or broad input-compatibility tests. Avoid promising a supported service based on these examples.

Release gate for adapting a recipe: pin the input repository and toolchain, run the original assertion, apply a controlled regression, confirm the expected diagnostic, and retain the CI evidence. Recheck branch protection if matrix context names change.

Security evidence includes the redacted historical secret scan in SECRET_AUDIT.md and HIGH/CRITICAL CI filesystem scanning. A full semantic security assessment and complete transitive dependency licensing inventory remain open.