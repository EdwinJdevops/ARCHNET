import unittest
from scripts.check_infrastructure_safety import check_source

def rule(start, end, cidrs='"0.0.0.0/0"', protocol="tcp"):
    return f'''ingress {{
      from_port = {start}
      to_port = {end}
      protocol = "{protocol}"
      cidr_blocks = [{cidrs}]
    }}'''

class IngressTests(unittest.TestCase):
    def test_public_ssh_denied(self):
        self.assertTrue(check_source(rule(22, 22)))

    def test_public_kubernetes_api_denied(self):
        self.assertTrue(check_source(rule(6443, 6443)))

    def test_port_range_denied(self):
        self.assertTrue(check_source(rule(1, 65535)))

    def test_public_https_allowed(self):
        self.assertFalse(check_source(rule(443, 443)))

    def test_private_ssh_allowed_by_narrow_guard(self):
        self.assertFalse(check_source(rule(22, 22, '"10.0.0.0/8"')))

    def test_unresolved_public_port_denied(self):
        self.assertTrue(check_source('ingress { from_port = var.port to_port = 6443 protocol = "tcp" cidr_blocks = ["0.0.0.0/0"] }'))

    def test_no_inline_rules_requires_review(self):
        self.assertTrue(check_source('resource "aws_security_group" "example" {}'))

if __name__ == "__main__":
    unittest.main()
