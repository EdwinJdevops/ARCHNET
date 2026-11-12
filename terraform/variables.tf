variable "enable_cloud_deployment" {
  description = "Cloud provisioning is disabled."
  type        = bool
  default     = false
  nullable    = false

  validation {
    condition     = var.enable_cloud_deployment == false
    error_message = "Cloud deployment is intentionally disabled."
  }
}
