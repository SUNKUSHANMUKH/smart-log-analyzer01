terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "log_system" {
  metadata {
    name = "log-system"
  }
}

resource "kubernetes_deployment" "log_app" {
  metadata {
    name      = "log-app-tf"
    namespace = kubernetes_namespace.log_system.metadata[0].name
  }
  spec {
    replicas = 2
    selector {
      match_labels = { app = "log-app" }
    }
    template {
      metadata {
        labels = { app = "log-app" }
      }
      spec {
        container {
          name  = "log-app"
          image = "smart-log-app:v1"
          image_pull_policy = "Never"
          port {
            container_port = 8000
          }
        }
      }
    }
  }
}
