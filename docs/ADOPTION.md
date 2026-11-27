# Evaluate the IAM recipe

Use a disposable Ubuntu GitHub-hosted runner with Bash, Python 3, sudo, unshare and Terraform 1.12.2. Dependencies download before the test enters a network namespace. No real cloud credentials are needed.

## Reproduce

Copy .github/workflows/uktrade-iam.yml into a test repository and open a pull request. Checkout deliberately selects UK Trade commit 40708174258425b82d845951245a311de7a73f0a. Expect a passing original and a failing mutation with ARCHNET_CREATE_ROLE_MISSING. The job succeeds only when both outcomes match.

The negative control edits the disposable checkout. Use an ephemeral workspace.

## Adapt

1. Select your repository, pinned revision and module directory.
2. Replace variables extraction with explicit non-secret module inputs.
3. Target your IAM policy data source and preserve its real renderer. Override only cloud lookups it depends on.
4. Assert on the exact action, resource or principal you need.
5. Mutate that source and require the expected assertion diagnostic.
6. Confirm the original passes and the mutation fails with networking disabled after setup.

Targeted planning covers the selected policy and its dependencies. Full infrastructure behavior requires additional acceptance tests.

## Compare fairly

Use the same pinned module, machine and assertion for native Terraform and an ARCHNET adaptation. Record setup minutes from a clean checkout, minutes to diagnose the mutation, configuration lines and files authored, and required positive-case module edits. Both paths must accept the original and reject the mutation for the expected reason.

Separate dependency installation and CI runtime from human setup effort. All independent human setup measurements remain uncollected. The current recipe uses native Terraform. A separate ARCHNET runtime has not demonstrated an advantage.

Share a public issue with a pinned commit, commands, redacted output and measured effort if you want to contribute evidence. Keep credentials and private code out of reports.
