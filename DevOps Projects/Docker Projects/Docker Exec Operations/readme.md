One of the Nautilus DevOps team members was working to configure services on a kkloud container that is running on App Server 1 in Stratos Datacenter. Due to some personal work he is on PTO for the rest of the week, but we need to finish his pending work ASAP. Please complete the remaining work as per details given below:

a. Install apache2 in kkloud container using apt that is running on App Server 1 in Stratos Datacenter.

b. Configure Apache to listen on port 6400 instead of default http port. Do not bind it to listen on specific IP or hostname only, i.e it should listen on localhost, 127.0.0.1, container ip, etc.

c. Make sure Apache service is up and running inside the container. Keep the container in running state at the end.

Solution:

ssh tony@stapp01
docker ps -a  
docker exec -it kkloud /bin/bash  
apt update -y  
apt install apache2 -y  
cd /etc/apache2  
vi ports.conf  
change port 80 to 6400 in ports.conf
change ServerName to lcoalhost  
service apache2 start    
service apache2 status  
exit 