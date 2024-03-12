# code-server

- rpm -ivh <package of the software> 

\#install the software 

 

- systemctl enable --now code-server@$USER 

\#启动Code-Server服务 

 

/root/.config/code-server/config.yaml 

修改bind-addr和password，之后重启并打开防火墙 

 

- systemctl restart code-server@$USER 
- firewall-cmd --add-port=8080/tcp --permanent 
- firewall-cmd --reload 

# passwd

- passwd 

修改密码 



# firewall-cmd

- firewall-cmd --add-port=80/tcp --permanent 

\#open 80 port 

 

- firewall-cmd --reload 

\#reload the firewall 

# ss

ss -ntl 

# Nginx

- yum -y install epel-release 

\#安装扩展软件仓库 

- yum -y install nginx 

\#install Nginx 

 

- systemctl enable --now nginx 

\#开机启动nginx并当即生效 

 

- firewall-cmd --add-port=80/tcp --permanent 
- firewall-cmd --reload 

\#open port and reload the firewall 

 

/usr/share/nginx/html 为默认nginx的网页文件夹 

 

- mkdir -p /web/fish 

\#创建存放网页代码的目录 

 

修改/etc/nginx/conf.d/fish.conf 
```ini
server { 
    listen 80; 
    server_name 192.168.140.128; 
    root /web/fish; 
    location / { 
        index index.php index.html; 
     } 

    location ~ \.php$ { 
        fastcgi_pass 127.0.0.1:9000; 
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name; 
        include fastcgi_params; 
     } 
} 
```

- nginx -t 

\#检查语法是否有错误 

 

- systemctl restart nginx 

\#重启 

 

- setenforce 0 

\#关闭selinux 

 

/etc/nginx/conf.d/usj.conf 

```ini
server { 
    listen 80; 
    server_name ehall.ujs.edu.cn; 
    root /web/ujs; 
    location / { 
        index index.php index.html; 
    } 
    location ~ \.php$ { 
        fastcgi_pass 127.0.0.1:9000; 
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name; 
        include fastcgi_params; 
     } 
} 
```

- systemctl restart nginx 

# selinux

/etc/selinux/config 

- setenforce 0 

# mysql

- mysqladmin -u<root> password '<password>' 

\#set the password for user 

 

- mysql -u<user> -p<password> 

\#login to the database 

 

- create database <database>; 
- drop database <database>; 

 

- use <database> 

\#select one database 

 

- show tables; 

\#show all tables in the database 

 

- create table user( 

id int primary key auto_increment, 

name varchar(255), 

gender varchar(255), 

hobby varchar(255) 

)default char set utf8; 

\#create a table and set columns 

 

- select name,gender from user; 
- select * from user where id=1; 
- select * from user where id=1 and gender="male"; 

 

- delete from user; 

\#delete all data from user 

 

- delete from user where id=1; 

\#delete the data which id quals 1 

 

- truncate user; 

\#恢复user到初始状态 

 

- update user set gender="female" where id=2; 

\#update the data 

 

- select * from <table> 

\#show all data from particular table 