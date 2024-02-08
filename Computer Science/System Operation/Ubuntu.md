# Code-Server

- systemctl enable --now code-server@$USER 

/root/.config/code-server/config.yaml 

修改IP和password 

- systemctl restart code-server@$USER 

- firewall-cmd --zone=public --add-port=8080/tcp --permanent 
- firewall-cmd --reload 

# GCC

- apt update 
- apt install build-essential 

- gcc --version 
- g++ --version 

\#check the version of gcc & g++ 

# php

- apt update 
- apt install php-fpm 
- systemctl status php7.4-fpm 

- apt install php-mysql php-gd 

\#install the extension of php 

/var/www/html 

create a php file and test weather it is working 

<?php 

phpinfo(); 

\> 

# firewall-cmd

- apt update 
- apt -y install firewalld 

\#install firewalld 

- firewall-cmd --zone=public --add-port=80/tcp --permanent 
- firewall-cmd --reload 

\#open port 80 and reload the firewall 

- firewall-cmd --zone=public --list-ports 
- firewall-cmd --state 

# Nginx

- apt update 
- apt install nginx 

\#install Nginx 

- systemctl enable --now nginx 
- systemctl status nginx 

\#check the status of nginx 

# MariaDB

- apt update 
- apt install mariadb-server 
- systemctl status mariadb 

- mysqladmin -uroot password <password> 
- mysql -uroot -p<password> 

\#login to the database 

# man

- man sqrt 

\#查看sqrt库函数的手册 

 

 