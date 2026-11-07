output "k3s_public_ip" {
  value       = try(aws_instance.k3s[0].public_ip, null)
  description = "Null while cloud deployment is disabled"
}
