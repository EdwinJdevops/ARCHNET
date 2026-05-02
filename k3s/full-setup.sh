#!/bin/bash
set -e
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml

# System setup
apt-get update
apt-get upgrade -y
apt-get install -y curl wget git

# Install k3s
curl -sfL https://get.k3s.io | sh -
sleep 15

# Wait for k3s to be ready
until kubectl get nodes &> /dev/null; do sleep 5; done

# Add Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Install ArgoCD namespace
kubectl create namespace argocd

# Install ArgoCD
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Wait for ArgoCD
sleep 30
until kubectl get deploy -n argocd argocd-server &> /dev/null; do sleep 5; done

# Patch ArgoCD to use LoadBalancer (since we're on EC2)
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'

# Create kubeconfig for user
mkdir -p /home/ubuntu/.kube
cp /etc/rancher/k3s/k3s.yaml /home/ubuntu/.kube/config
sed -i "s/127.0.0.1/$(hostname -I | awk '{print $1}')/g" /home/ubuntu/.kube/config
chown -R ubuntu:ubuntu /home/ubuntu/.kube

echo "k3s and ArgoCD ready"
