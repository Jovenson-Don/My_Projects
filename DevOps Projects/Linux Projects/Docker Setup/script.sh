sudo -i

# Add a local DNS entry for the database hostname "mydb.kodekloud.com" so that it can resolve to "10.0.0.50" IP address.
echo "10.0.0.50    mydb.kodekloud.com" >> /etc/hosts

# Add an extra IP to "eth1" interface on this system: 10.0.0.50/24
ip address add 10.0.0.50/24 dev eth1

# Install "mariadb" database server on this server and "start/enable" its service.
yum install mariadb-server -y
systemctl enable mariadb
systemctl start mariadb

# Set a password for mysql root user to "S3cure#321"
mysqladmin -u root password 'S3cure#321'

# The "root" account is currently locked on "centos-host", please unlock it.
usermod -U root

# Make user "root" a member of "wheel" group
usermod -G wheel root

# Pull "nginx" docker image.
docker pull nginx

# docker-container
docker run -d -p 80:80 --name myapp nginx

# container-start.sh
cat <<EOF > /home/bob/container-start.sh
#!/usr/bin/env bash

docker start myapp
echo "myapp container started!"
EOF
chmod +x /home/bob/container-start.sh

# container-stop.sh
cat <<EOF > /home/bob/container-stop.sh
#!/usr/bin/env bash

docker stop myapp
echo "myapp container stopped!"
EOF
chmod +x /home/bob/container-stop.sh


# Add a cron job for the "root" user which should run "container-stop.sh" script at "12am" everyday.
(crontab -l 2>/dev/null; echo "0 0 * * * /home/bob/container-stop.sh") | crontab -
# Add a cron job for the "root" user which should run "container-start.sh" script at "8am" everyday.
(crontab -l 2>/dev/null; echo "0 8 * * * /home/bob/container-start.sh") | crontab -

# Edit the PAM configuration file for the "su" utility  ... etc.
# Here we have to uncomment both lines starting #auth
sed -i 's/#auth/auth/' /etc/pam.d/su
