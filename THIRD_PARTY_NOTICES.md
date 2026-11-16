# Third-party source

The IAM policy fixtures adapt policy blocks from two Apache-2.0 upstream projects. ARCHNET adds offline provider configuration, synthetic inputs and assertions, and substitutes fixed inputs for surrounding module logic. Upstream copyrights apply to the respective excerpts.

- `eks.tf.fixture` adapts [Terraform AWS EKS v20.37.2](https://github.com/terraform-aws-modules/terraform-aws-eks/blob/v20.37.2/main.tf).
- `cloudposse.tf.fixture` adapts [Cloud Posse EKS IAM Role](https://github.com/cloudposse/terraform-aws-eks-iam-role/blob/0c2347ca06fb54579a0e57d03e20aed3c1045157/main.tf).

External CI tools, including the Terraform CLI, remain under their respective licenses.
