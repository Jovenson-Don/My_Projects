
The Nautilus DevOps team is planning to host an application on a nginx-based container. There are number of tickets already been created for similar tasks. One of the tickets has been assigned to set up a nginx container on Application Server 1 in Stratos Datacenter. Please perform the task as per details mentioned below:

a. Pull nginx:stable docker image on Application Server 1.
b. Create a container named blog using the image you pulled.
c. Map host port 8089 to container port 80. Please keep the container in running state.

Solution
ssh tony@stapp01
docker run -d -p 8089:80 --name blog nginx:stable
# to confirm it worked
docker ps