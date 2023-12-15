resource "docker_image" "mariadb-image" {
  name = "mariadb:challenge"
  build {
    path = "lamp_stack/custom_db"

    label = {
    challenge:" second"
    }
  }
}

resource "docker_volume" "mariadb_volume" {
  name = "mariadb-volume"
}

resource "docker_container" "phpmyadmin" {
  depends_on = [docker_container.mariadb]
  image = "phpmyadmin/phpmyadmin"
  name  = "db_dashboard"
  hostname = "phpmyadmin"
  networks_advanced {
    name = docker_network.private_network.name
  }
  ports {
    internal = 80
    external = 8081
    ip = "0.0.0.0"
  }
  labels {
    label = "challenge"
    value = "second"
  }
  links = [docker_container.mariadb.hostname]
}

resource "docker_container" "mariadb" {
  image = "mariadb:challenge"
  name  = "db"
  hostname = "db"
  networks_advanced {
    name = docker_network.private_network.name
  }
  ports {
    internal = 3306
    external = 3306
    ip = "0.0.0.0"
  }
  env = ["MYSQL_ROOT_PASSWORD=1234", "MYSQL_DATABASE=simple-website"]
  volumes {
    volume_name = docker_volume.mariadb_volume.name
    container_path = "/var/lib/mysql"
  }
  labels {
    label = "challenge"
    value = "second"
  }
}