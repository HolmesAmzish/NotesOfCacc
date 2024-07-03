# Linux结课报告

## 实验目的

部署Wordpress和其他若干开源项目到虚拟机中。首先需要配置LNMP环境，在Linux系统下载并安装Nginx（Apache2）、MySQL（MariaDB）、PHP和相关插件。

使用VMware Workstation Pro作为虚拟机软件，并安装了虚拟机系统Debian 12。还有部分操作在MobaXterm和Visual Studio Code上完成，分别作为SSH终端和文件编辑工具。

对于实现公网访问的一些扩展内容，使用了frp内网穿透工具，以及阿里云提供的云服务器和域名解析。

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

### 配置Wordpress

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

### Z-Blog

#### 下载和创建网站

首先下载网站，搜索后根据官方文档，下载压缩包https://www.zblogcn.com/program/zblogphp17/。移动到`/var/www/zblog`并解压。

```bash
unzip Z-BlogPHP_1_7_3_3290_Finch.zip -d /var/www/zblog
```

之后到nginx的配置文件中设置，编辑`/etc/nginx/sites-available/zblog.conf`设置如下

```ini
server {
    listen 81;
    server_name dev2.arorms.cn;

    root /var/www/zblog;
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

然后需要创建链接到sites-enabled以启用这个网站，随后重新加载nginx的设置。

```bash
ln -s /etc/nginx/sites-available/zblog.conf /etc/nginx/sites-enabled/
nginx -t
systemctl reload nginx
```

![image-20240702191721030](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702191721030.png)

<center>图16 Nginx设置和下载好的原代码</center>

#### 网站的安装

完成以上步骤后，浏览器访问相应url就可以看到刚刚部署的网站，根据我的设置，应该访问`http://dev2.arorms.cn:81`，可以看到进入安装程序。

![image-20240702193352875](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702193352875.png)

<center>图17 Z-blog安装程序</center>

检测好服务器系统环境之后，跳转到数据库建立与设置，这里也是首先手动建立数据库。

```bash
mysql -uroot -p123456
```

```sql
CREATE DATABASE zblog;
EXIT;
```

![image-20240702193714486](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702193714486.png)

<center>图18 创建数据库</center>

![image-20240702193641379](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702193641379.png)

<center>图19 网站设置</center>

随后继续下一步，发现安装程序出错，需要手动创建脚本，根据提示创建一个php脚本并将代码黏贴进去。

![屏幕截图 2024-07-02 194010](C:\Users\Holme\Pictures\Screenshots\屏幕截图 2024-07-02 194010.png)

<center>图20 网站手动设置脚本提示</center>

保存后重新进入即可。其次可能还会显示编译文件不存在的错误，通过网络搜索找到了原因在于没有对`/zb_users/cache`文件夹的读写权限，通过修改权限即可解决问题。

```bash
chmod -R 777 /var/www/zblog/zb_users/cache
# 修改cache的权限，并应用于子项
```

![image-20240702195338599](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702195338599.png)

<center>图21 部署完成</center>

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

<center>图22 nginx设置</center>

#### 下载网站文件

通过网络搜索，找到了项目地址https://github.com/typecho/typecho。

```bash
cd /var/www/
git clone git@github.com:typecho/typecho.git
```

这里由于是新创建的机器，所以好像因为没有配置密钥对所以无法连接至github，需要手动配置一个。

![image-20240703091931080](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703091931080.png)

<center>图23 无法连接至github</center>

```bash
cd ~/.ssh
ssh-keygen
# 生成密钥对
```

一路回车即可，然后查看pub文件结尾的公钥，复制到github上。

![image-20240703092051709](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703092051709.png)

<center>图24 创建好的密钥对</center>

![image-20240703092310374](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703092310374.png)

<center>图25 添加好的公钥</center>

然后下载完毕

![image-20240703092403329](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703092403329.png)

<center>图26 下载好的网站文件</center>

#### 设置网站

访问`dev2.arorms.cn:82`即可看到网站的安装页面

![image-20240703092605314](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703092605314.png)

<center>图27 网站安装页面</center>

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

<center>图28 创建数据库</center>

![image-20240703093103884](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703093103884.png)

<center>图29 数据库信息填写和脚本创建</center>

```bash
touch /var/www/typecho/config.inc.php
# 然后通过MobXterm左边的SFTP直接将代码写入
```

随后是一些基本设置

![image-20240703093526215](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703093526215.png)

<center>图30 基本设置</center>

然后访问发现部署成功

![image-20240703093553076](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240703093553076.png)

<center>图31 部署成功</center>

### FRP内网穿透

IPv4地址在2019年已分配完毕，今天的个人设备很难拥有一个IPv4地址。而IPv6地址尚未普及，很多情况下还无法访问IPv6的网络。如果想要将项目部署到公网上，必须需要一个公网IP地址。一般来说云平台提供的云服务器都会带有IP地址，可以实现直接访问。而如果是自己的机器或者虚拟机，通常是没有公网IP的，所以需要通过一个在公网下的服务器，将数据转发给客户端和服务端，来实现将项目部署到互联网上，实现公网访问，这里以刚刚实验的虚拟机为例子。

#### 设置FRP服务端

首先需要下载FRP，地址在github上https://github.com/fatedier/frp。FRP服务端需要一个有公网IP的服务器，这里我有一个阿里云的云服务器作为转发数据的服务器，系统是FreeBSD。首先现在服务器下载好相应软件。

![image-20240702201811927](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702201811927.png)

<center> 图32 云服务器信息</center>

![image-20240702200750999](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702200750999.png)

<center>图33 下载好的服务端</center>

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

<center>图34 下载好的客户端</center>

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

<center>图35 运行成功</center>

这里我设置的是根据域名转发，所以需要前往域名解析修改，将域名解析指向代理的云服务器。

![image-20240702205356186](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702205356186.png)

<center>图36 域名解析修改</center>

这里已经将wordpress.arorms.cn解析到了云服务器的地方，浏览器访问`http://wordpress.arorms.cn`并且是公网访问，已经可以访问到。

![image-20240702205722099](C:\Users\Holme\AppData\Roaming\Typora\typora-user-images\image-20240702205722099.png)



<center>图37 公网访问成功</center>

## 实验总结

