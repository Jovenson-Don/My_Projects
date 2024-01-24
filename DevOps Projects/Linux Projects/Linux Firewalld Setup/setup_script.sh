#!/bin/bash

#after ssh into each service and with sudo rights
sudo yum install firewalld -y
systemctl start firewalld
systemctl enable firewalld
systemctl status firewalld
systemctl status nginx
systemctl status httpd
firewall-cmd --add-port 80/tcp --permanent --zone public
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" port port="8080" protocol="tcp" reject'
firewall-cmd reload

