FROM ubuntu:latest
RUN apt update && apt install apache2 -y
RUN sed -i "s/80/8088/" /etc/apache2/ports.conf
EXPOSE 8088/tcp
CMD ["apache2ctl", "-D", "FOREGROUND"]