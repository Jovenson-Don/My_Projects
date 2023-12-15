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
  network_alias =  ["my_network"]
  ports {
    internal = 80
    external = 80
    ip = "0.0.0.0"
  }
}