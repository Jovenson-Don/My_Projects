resource "kubernetes_service" "webapp-service" {
  metadata {
    name = "webapp-service"
  }
  spec {
    type = "NodePort"
    port {
      port = 8080
      node_port = 30080
    }
  }
}