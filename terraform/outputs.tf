output "namespace" {
  value = kubernetes_namespace.log_system.metadata[0].name
}
