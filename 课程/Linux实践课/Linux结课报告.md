# Linux结课报告

## 实验目的

实验的主要目的是通过在虚拟机中部署WordPress及其他若干开源项目，掌握LNMP（Linux, Nginx, MySQL, PHP）环境的搭建和配置。在Linux系统中下载并安装Nginx（或Apache2）、MySQL（MariaDB）、PHP及相关插件，确保这些组件可以协同工作。此外，实验中还将使用VMware Workstation Pro作为虚拟机软件，部署Debian 12操作系统，借助MobaXterm和Visual Studio Code等工具进行SSH终端连接和文件编辑。

## 实验内容

### 环境配置

实验中我使用了LNMP环境作为实验环境。

#### Nginx

```bash
apt update
apt install nginx -y
# 下载Nginx

systemctl disable --now apache2
apt purge apache2
apt autoremove
# 删除系统自带的apache2

systemctl enable --now nginx
systemctl status nginx
# 设置nginx开机自启动并检查
```



![image-20240630105550865](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630105550865.png)

<center>图1 Nginx完成安装</center>


![image-20240630110133191](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630110133191.png)

<center>图2 Nginx浏览器访问</center>

#### MariaDB

下载MariaDB并设置。

```bash
apt install mariadb-server -y
mysqladmin password '123456'
# 设置密码
mysql -uroot -p123456
```

```sql
SHOW DATABASES;
# 显示当前所有数据
```

![image-20240630110509029](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630110509029.png)

<center>图3 数据库的安装</center>

#### PHP

安装PHP和所需插件

```bash
apt install -y php8.2 php8.2-{fpm,cli,common,mysql,xml,curl,gd,mbstring,zip,bcmath,intl,soap,imap,opcache}
```

测试php是否可用，首先需要到网站的设置文件中启用php，将php结尾的页面传送给php服务端。文件位于`/etc/nginx/sites-available/default`

```ini
server {
    listen 80;
    server_name default_server;

    root /var/www/html;
    index index.php index.html index.htm index.nginx-debian.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php8.2-fpm.sock;
    }

    location ~ /\.ht {
        deny all;
    }
}
```

重新加载Nginx的设置

```bash
nginx -t
systemctl reload nginx
```

![image-20240630111823375](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630111823375.png)

<center>图4 重新加载php</center>

随后编辑一个php脚本用于测试是否可以正常访问服务器的php页面。

`/var/www/html/info.php`

```php
<?php phpinfo(); ?>
```

然后打开浏览器访问对应的URL，就可以查看php信息。

![image-20240630111948833](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630111948833.png)

<center>图5 PHP信息页面</center>

### Wordpress

#### 网站设置

首先需要新建一个Nginx的网站设置文件，可以直接将原来的设置复制过来。在同一个服务器下的网站需要不同标签分辨开来。可以使用端口，但是唯一不足就是需要记住不同的端口。另一种方法就是利用不同域名来区分，为不同网站分配不同的子域名。在实验中使用这个方法来进行设置。在这里没有设置端口映射，暂时先指向一个内网IP。

![image-20240630112858588](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630112858588.png)

<center>图6 分配子域名</center>

然后在Nginx处设置网站`/etc/nginx/sites-available/wordpress.conf`

```ini
server {
    listen 80;
    server_name wordpress.arorms.cn;

    root /var/www/wordpress;
    index index.php index.html index.htm index.nginx-debian.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php8.2-fpm.sock;
    }

    location ~ /\.ht {
        deny all;
    }
}
```

然后启用网站

```bash
ln -s /etc/nginx/sites-available/wordpress.conf /etc/nginx/sites-enabled/
nginx -t
systemctl reload nginx
```

![image-20240630114214582](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630114214582.png)

<center>图7 启用网站</center>

#### 下载WordPress

根据设置，首先前往目录`/var/www/`然后下载wordpress

```bash
cd /var/www
wget https://wordpress.org/latest.tar.gz
tar -xvf latest.tar.gz
```

![image-20240630113534384](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630113534384.png)

<center>图8 下载并解压wordpress</center>

#### 设置WordPress

现在可以通过浏览器访问到刚刚部署的WordPress，访问`wordpress.arorms.cn`即可看见相关页面。

![image-20240630114359898](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630114359898.png)

<center>图9 访问部署的WordPress</center>

![image-20240630115004523](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630115004523.png)

<center>图10 数据库设置</center>

在图10中，需要到终端手动设置数据库并填入相关信息。

```bash
mysql -uroot -p123456
```

```SQL
CREATE DATABASE wordpress;
CREATE USER 'wordpress'@'localhost' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

![image-20240630115651778](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630115651778.png)

<center>图11 设置数据库</center>

![image-20240630115734999](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630115734999.png)

<center>图12 手动安装脚本</center>

此处提示无法直接写入wp-config.php脚本，需要手动到网站根目录下编辑这样一个脚本文件。`/var/www/wordpress/wp-config.php`

![image-20240630120003151](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630120003151.png)

<center>图13 手动写入</center>

然后安装。随后是一些基本的站点信息设置，最后完成WordPress的部署。

#### WordPress的使用

![image-20240630121531020](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630121531020.png)

<center>图14 WordPress的仪表盘</center>

![image-20240630121508613](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240630121508613.png)

<center>图15 WordPress的帖子编辑页面</center>

### Typecho

#### 设置网站

```bash
cd /etc/nginx/sites-available/
vim typecho.conf
# 编辑一个新的typecho.conf
```

```ini
server {
    listen 82;
    server_name dev2.arorms.cn;

    root /var/www/typecho;
    index index.php index.html index.htm;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php8.2-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }

    location ~ /\.ht {
        deny all;
    }
}
```

设置完成后检查并重新加载

```bash
nginx -t
systemctl reload nginx
```

![image-20240703091557910](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703091557910.png)

<center>图16 nginx设置</center>

#### 下载网站文件

通过网络搜索，找到了项目地址https://github.com/typecho/typecho。

```bash
cd /var/www/
git clone git@github.com:typecho/typecho.git
```

这里由于是新创建的机器，所以好像因为没有配置密钥对所以无法连接至github，需要手动配置一个。

![image-20240703091931080](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703091931080.png)

<center>图17 无法连接至github</center>

```bash
cd ~/.ssh
ssh-keygen
# 生成密钥对
```

一路回车即可，然后查看pub文件结尾的公钥，复制到github上。

![image-20240703092051709](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703092051709.png)

<center>图18 创建好的密钥对</center>

![image-20240703092310374](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703092310374.png)

<center>图19 添加好的公钥</center>

然后下载完毕

![image-20240703092403329](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703092403329.png)

<center>图20 下载好的网站文件</center>

#### 设置网站

访问`dev2.arorms.cn:82`即可看到网站的安装页面

![image-20240703092605314](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703092605314.png)

<center>图21 网站安装页面</center>

对于图中问题，前往网站根目录，在/usr文件夹中创建uploads文件夹并调整权限。

```bash
mkdir /var/www/typecho/usr/uploads
chmod 777 /var/www/typecho/usr/uploads
```

下一步前往到数据库设置页面，在终端创建一个新的数据库。

```bash
mysql -uroot -p123456
```

```sql
CREATE DATABASE typecho;
EXIT;
```

![image-20240703092941043](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703092941043.png)

<center>图22 创建数据库</center>

![image-20240703093103884](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703093103884.png)

<center>图23 数据库信息填写和脚本创建</center>

```bash
touch /var/www/typecho/config.inc.php
# 然后通过MobXterm左边的SFTP直接将代码写入
```

随后是一些基本设置

![image-20240703093526215](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703093526215.png)

<center>图24 基本设置</center>

然后访问发现部署成功

![image-20240703093553076](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703093553076.png)

<center>图25 部署成功</center>

### FRP内网穿透

IPv4地址在2019年已分配完毕，今天的个人设备很难拥有一个IPv4地址。而IPv6地址尚未普及，很多情况下还无法访问IPv6的网络。如果想要将项目部署到公网上，必须需要一个公网IP地址。一般来说云平台提供的云服务器都会带有IP地址，可以实现直接访问。而如果是自己的机器或者虚拟机，通常是没有公网IP的，所以需要通过一个在公网下的服务器，将数据转发给客户端和服务端，来实现将项目部署到互联网上，实现公网访问，这里以刚刚实验的虚拟机为例子。

#### 设置FRP服务端

首先需要下载FRP，地址在github上https://github.com/fatedier/frp。FRP服务端需要一个有公网IP的服务器，这里我有一个阿里云的云服务器作为转发数据的服务器，系统是FreeBSD。首先现在服务器下载好相应软件。

![image-20240702201811927](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702201811927.png)

<center> 图26 云服务器信息</center>

![image-20240702200750999](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702200750999.png)

<center>图27 下载好的服务端</center>

其中，要编辑frp服务端的设置。

```toml
bindPort = 7000
vhostHTTPPort = 80

webServer.addr = "0.0.0.0"
webServer.port = 7500
webServer.user = "admin"
webServer.password = "admin"
```

开启

```bash
./frps -c ./frps.toml
```

设置开机自启动，需要编辑`/usr/local/etc/rc.d/frp`

```ini
#!/bin/sh

# PROVIDE: frps
# REQUIRE: NETWORKING
# KEYWORD: shutdown

. /etc/rc.subr

name="frps"
rcvar="frps_enable"

start_cmd="${name}_start"
stop_cmd="${name}_stop"

frps_start() {
    echo "Starting frps..."
    nohup /root/frp/frps -c /root/frp/frps.toml >/dev/null 2>&1 &
    # 将所有输出丢弃
}

frps_stop() {
    echo "Stopping frps..."
    pkill -f "/root/frp/frps -c /root/frp/frps.toml"
}

load_rc_config $name
run_rc_command "$1"
```

随后到`/etc/rc.conf`中启用这个脚本

```ini
frp_enable="YES"
```

开启frp

```bash
service frp start
```

#### 设置FRP客户端

首先在github上下载完成后，将文件上传到/opt文件夹中，并解压。

![image-20240702204107781](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702204107781.png)

<center>图28 下载好的客户端</center>

然后编辑frpc.toml，这是客户端的设置文件

```toml
serverAddr = "inf3.arorms.cn"
serverPort = 7000

[[proxies]]
name = "dev2-http"
type = "http"
localPort = 80
customDomains = ["wordpress.arorms.cn"]
```

随后设置服务，编辑service文件，在`/usr/lib/systemd/system`新建一个frp-http.service

```ini
[Unit]
Description=Frp Client Service
After=network.target

[Service]
Type=simple
User=nobody
Restart=on-failure
RestartSec=5s
ExecStart=/opt/frp_0.58.1_linux_amd64/frpc -c /opt/frp_0.58.1_linux_amd64/frpc.toml

[Install]
WantedBy=multi-user.target
```

然后启动并检查服务即可

```bash
systemctl enable --now frp
systemctl status frp
```

![image-20240702205134204](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702205134204.png)

<center>图29 运行成功</center>

这里我设置的是根据域名转发，所以需要前往域名解析修改，将域名解析指向代理的云服务器。

![image-20240702205356186](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702205356186.png)

<center>图30 域名解析修改</center>

这里已经将wordpress.arorms.cn解析到了云服务器的地方，浏览器访问`http://wordpress.arorms.cn`并且是公网访问，已经可以访问到。

![image-20240702205722099](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702205722099.png)



<center>图31 公网访问成功</center>

## 实验总结

通过本次实验，我在虚拟机中成功部署了WordPress及其他若干开源项目，并完成了LNMP（Linux, Nginx, MySQL, PHP）环境的搭建和配置任务。本实验不仅仅是对LNMP环境搭建的实践，更是对Linux系统操作、服务器配置以及网络访问的一次全面学习和深入探索。

首先，我选择了VMware Workstation Pro作为虚拟机软件，并安装了Debian 12操作系统。在实验的初期，我通过MobaXterm和Visual Studio Code进行SSH连接和文件编辑，这些工具大大提升了远程操作的效率和便捷性。配置过程中，我依次安装了Nginx、MariaDB和PHP，并确保这些组件可以正常协同工作。特别是对于Nginx的配置，我详细设置了相关的启动项和服务状态，确保其在系统启动时自动加载并运行稳定。

在安装MariaDB数据库时，我不仅设置了数据库的基本配置，还手动创建了所需的数据库和用户，授予了相应的权限，以确保WordPress能够正确连接和操作数据库。在PHP的安装过程中，我安装了多个必要的扩展插件，并测试了PHP的可用性，确保Web服务器能够正确解析和执行PHP脚本。

由于大多数个人设备无法获得独立的IPv4地址，我通过使用frp内网穿透工具解决了这一问题。通过配置frp服务端和客户端，实现了虚拟机内项目的公网访问。这部分内容不仅包括了对frp的安装和配置，还涉及了阿里云服务器的使用和域名解析的设置。通过这些操作，我成功地将虚拟机中的项目部署到了互联网上，使其能够被外界访问。

此外，在实验中我还部署了Typecho等其他开源项目，并进行了类似的配置和测试，进一步巩固了对LNMP环境的掌握。在配置过程中，遇到的一些问题也让我对Linux系统和网络配置有了更深的理解，例如如何处理权限问题、如何设置文件路径及如何进行网络端口的配置等。

通过本次实验，我不仅掌握了LNMP环境的搭建和配置技能，还学会了如何在实际操作中排查和解决问题。这些实践经验对于今后进一步学习和工作具有重要的指导意义。同时，本次实验也让我认识到，服务器配置和网络访问是一个系统性的工程，需要综合运用多方面的知识和技能。总体而言，这次实验为我提供了一个全面而深入的学习平台，使我对Linux服务器管理和Web应用部署有了更深刻的理解和更强的实践能力。
