# Secret audit evidence

On 24 November 2026, Gitleaks v8.30.1 scanned all locally fetched Git refs, including release tags, using --log-opts=--all and redacted reporting. The downloaded executable matched its published SHA-256 checksum. The run scanned 37 commits and reported no leaks.

GitHub secret scanning and push protection are enabled. No open secret alerts were returned during inspection. This result covers fetched Git history and configured detection rules. It does not cover external services, deleted unreachable objects, or credentials outside the repository.

The existing CI HIGH/CRITICAL filesystem scan passed on the last merged code. A comprehensive semantic security review is still outstanding. A full transitive dependency license review and CNCF eligibility determination are also open.
