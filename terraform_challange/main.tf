resource "docker_image" "php-httpd-image" {
  name = "php-httpd:challenge"
  build {
    path = "lamp_stack/php_httpd"

    label = {
      challenge: "second"
    }
  }
}

resource "docker_container" "php-httpd" {
  name = "webserver"
  hostname = "php-httpd"
  image = docker_image.php-httpd-image.name
  networks_advanced {
    name = docker_network.private_network.name
  }
  ports {
    internal = 80
    external = 80
    ip = "0.0.0.0"
  }
  labels {
    label = "challenge"
    value = "second"
  }
  volumes {
    host_path = "/root/code/terraform-challenges/challenge2/lamp_stack/website_content/"
    container_path = "/var/www/html"
  }
}