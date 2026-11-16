# Offline IAM policy rendering experiment

The fixtures extract the trust policy renderer from [EKS v20.37.2](https://github.com/terraform-aws-modules/terraform-aws-eks/blob/v20.37.2/main.tf) and [Cloud Posse at 0c2347c](https://github.com/cloudposse/terraform-aws-eks-iam-role/blob/0c2347ca06fb54579a0e57d03e20aed3c1045157/main.tf). They supply fixed inputs for surrounding module logic and account identity. The actual AWS provider renders the document. The harness compares a principal in its generated JSON before and after changing a renderer input.

CI downloads the provider before testing. Plans run in a separate Linux network namespace with an empty environment and literal dummy credentials. The fixtures declare no managed resources and the harness runs only plans. The experiment tests isolated policy rendering. It does not establish that complete upstream modules can plan without cloud reads, that the policies are production-ready, or that maintainers need a new tool.
