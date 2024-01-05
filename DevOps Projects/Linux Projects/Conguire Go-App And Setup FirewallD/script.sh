sudo -i

## Fix yum DNS errors by inserting google nameserver
# Can't use sed -i here as we get "Device or resource busy"
sed '1inameserver 8.8.8.8' /etc/resolv.conf > /tmp/resolv.conf

# Can't use cp or mv for the same reason
cat  /tmp/resolv.conf > /etc/resolv.conf

yum install -y nginx firewalld

# Start and Enable "firewalld" service.
systemctl enable firewalld
systemctl start firewalld

# Add firewall rules to allow only incoming port "22", "80" and "8081" and make permanent
firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --zone=public --add-port=8081/tcp --permanent
firewall-cmd --zone=public --add-port=22/tcp --permanent
firewall-cmd --reload

# Start GoApp by running the "nohup go run main.go &" command from "/home/bob/go-app/" directory
pushd /home/bob/go-app
nohup go run main.go &

# Wait for it to be running (usually 15-20 seconds as it has to compile first)
while ! ps -faux | grep -P '/tmp/go-build\d+/\w+/exe/main'
do
    sleep 2
done
sleep 2
popd

# Configure Nginx as a reverse proxy for the GoApp so that we can access the GoApp on port "80"
# Do this by inserting a proxy_pass line after "location / {" at line 48
sed -i '48i\            proxy_pass  http://localhost:8081;' /etc/nginx/nginx.conf

# Start nginx
systemctl enable nginx
systemctl start nginx

# bob is able to login into GoApp using username "test" and password "test"
curl -u test:test http://localhost:80 || echo -e "\n\nBob cannot log in!"