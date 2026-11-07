variable "aws_region" {
  default = "us-east-1"
}

variable "instance_type" {
  default = "t3.medium"
}

variable "key_name" {
  description = "EC2 key pair name (must exist in AWS)"
  type        = string
}

variable "enable_cloud_deployment" {
  description = "Safety lock: cloud deployment is disabled until bootstrap, access and cost gates are implemented."
  type        = bool
  default     = false
  validation {
    condition     = var.enable_cloud_deployment == false
    error_message = "Cloud deployment is intentionally disabled pending audited bootstrap and cost review."
  }
}
