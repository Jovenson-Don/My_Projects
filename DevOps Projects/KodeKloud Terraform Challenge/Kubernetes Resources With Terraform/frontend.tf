resource "kubernetes_deployment" "frontend" {
  metadata {
    name = "frontend"
    labels = {
      name: "frontend"
    }
  }
  spec {
    selector {
      match_labels = {
        name = "webapp"
      }
    }
    replicas = "4"
    template {
      metadata {
        labels = {
          name = "webapp"
        }
      }
      spec {
        container {
          name = "simple-webapp"
          image = "kodekloud/webapp-color:v1"
          port {
            container_port = 80
          }
        }
      }
    }
  }
}