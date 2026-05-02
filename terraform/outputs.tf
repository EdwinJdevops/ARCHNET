output "k3s_public_ip" {
  value       = aws_instance.k3s.public_ip
  description = "Public IP of k3s master"
}

output "ssh_command" {
  value       = "ssh -i ~/.ssh/YOUR_KEY.pem ubuntu@${aws_instance.k3s.public_ip}"
  description = "SSH command"
}
