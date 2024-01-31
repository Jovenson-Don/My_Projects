resource "docker_image" "nginx" {
  name = "nginx:latest"
}

resource "docker_container" "nginx-container" {
  image = docker_image.nginx.name
  name = "nginx"
}
