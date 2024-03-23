# 守护进程

## 设置文件

`/usr/lib/systemd/system`

```ini
[Unit]
Description=StarryFrp Service
After=network.target

[Service]
Type=idle
User=nobody
Restart=on-failure
RestartSec=60s
ExecStart=/usr/local/bin/frpc -f c3867d3c81ee8403eeed309304ae192a:98285

[Install]
WantedBy=multi-user.target


```

## 启动服务

```bash
systemctl enable --now ***.service
```



# SSH

## 安装 SSH 服务器

Debian 默认安装了SSH服务器，如果发现系统没有安装过SSH，可以手动下载。

```bash
apt update
# 更新应用列表

apt install -y openssh-server
# 下载SSH服务器
```

## 检查和启用 SSH 服务器

```bash
systemctl status ssh
# 检查SSH服务器是否开启

systemctl enable --now ssh
# 手动设置SSH开机自启动和现在启动
```

还有其他选项用来手动设置SSH服务

```bash
system [option] ssh
```

| 选项    | 操作              |
| ------- | ----------------- |
| start   | 启动SSH           |
| stop    | 停止SSH           |
| enable  | 开机允许SSH自启动 |
| disable | 开机禁止SSH自启动 |
| restart | 重启SSH服务       |

*详情查看systemctl指令详细说明*

## 访问 SSH 服务器

首先在本地查询其IP，两个命令都可以显示IP

```bash
hostname -I
# 查询局域网IP

ip address
# 查询网卡信息
```

返回你的电脑，连接 Debian 的 SSH 服务器

```powershell
ssh username@ip-addr
# 以username 的身份登录 ip-addr
```

然后输入 yes 确认指纹，随后输入 username 的密码登录到 Debian 的 SSH 服务器

操作结束后，可以通过 exit 命令退出 SSH 服务器返回本地的命令行。

```bash
exit
```



## 启用远程 root 登录权限

SSH远程连接时可能无法直接通过root账户登录，会显示权限不足（Permission denied, please try again.）要开启root账户远程登录，找到`/etc/ssh/sshd_config` 文件并修改其中的设置，需要找到这两个设置并将参数修改为`yes`。

```bash
nano /etc/ssh/sshd_config
# 以nano打开sshd_config设置文件
```

```
PermitRootLogin yes
# 允许远程root登录

PasswordAuthentication yes
# 开启密码认证
```
![rootpermit](/img/13.png)

然后重启ssh服务器，使其设置生效。

```bash
systemctl restart ssh
```

## 修改端口

SSH 服务的默认端口为 22，如果你想要修改 SSH 服务的端口，还是前往SSH的设置文件（sshd_config）并修改他，将 port 一行的井号删除使其生效，并修改其参数22为你想要的端口。

![port](/img/14.png)

最后重启 SSH 服务即可生效。



# Web服务器

LAMP即Linux，Apache，Mysql，php

## Linux

安装Linux服务器以提供服务。可以使用公有云平台进行服务器部署，也可以在物理机上安装内网穿透。

## Apache

### 安装apache2

```bash
apt update
apt install nginx
```

通过systemctl查看apache是否运行，也可以通过第二行手动设置开机自启动

```bash
systemctl status nginx
systemctl enable --now nginx
```

### 配置子网站

设置文件`/etc/apache2/sites-avaliable/xxx.conf

```ini
<VirtualHost *:80>
        ServerName dev.val.arorms.cn
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/val.arorms.cn
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

然后启动虚拟机

```bash
a2ensite xxx.conf

# 如果a2ensite没有添加到PATH，可以指定位置
/usr/sbin/a2ensite xxx.conf
```

然后重新加载apache2服务

```bash
systemctl reload apache2
```





## PHP

首先安装PHP

```bash
apt install php
```

在安装PHP同时，还要安装好必要包。

```bash
apt install php libapache2-mod-php php-mysql
```



apache的默认网站根目录在/var/www/html
使用命令ls可以看到主页文件是index.html
在本文件夹touch创建一个文件phpinfo.php
文件内容如下：

```php
<?php
	phpinfo();
?>
```

随后在浏览器访问这个文件 xxx.xxx.xxx.xxx/phpinfo.php
如果本页面显示了php的信息，那么说明php已经安装成功



## MariaDB(MySQL)

Debian默认软件源并不包含MySQL软件包，取而代之的是MariaDB。这个具体原因是因为MySQL遭到了阉割，而MariaDB是原作者重新创建的，具体原因自行搜索

```bash
apt install mariadb-server

systemctl status mariadb
#查看mariaDB是否运行，而也可以通过下面指令手动改为开机自启动

systemctl enable --now mariadb
```

登录命令

```bash
mysql -uroot -p
# root是数据库用户，没有密码-p后不带参数
```



## *强制安装PHP7.4版本*

现在大多数系统安装源已经不支持7.4版本，但是众多软件与应用仍然以7.4为基础，为此，可以强制给系统安装PHP7.4环境，这样与原来的版本并不影响。首先要解决下载源的问题，按照下列指令添加下载源。

```bash
# 先更新软件源并升级
apt update && apt upgrade -y

# 安装software-properties-common软件管理器（这一步不是必须，有些发行版本已经安装好了）
apt install software-properties-common

# 增加 ondrej/php PPA，提供了多个 PHP 版本
add-apt-repository ppa:ondrej/php

# 再次更新
apt update
```

然后安装`php7.4`以及相关的扩展

```bash
apt install -y php7.4-fpm php7.4-mysql php7.4-dev \
php7.4-redis php7.4-gd php7.4-mbstring php7.4-zip \
php7.4-curl php7.4-sqlite3 php7.4-xml php7.4-yaml \
php7.4-decimal php7.4-http php7.4-imagick php7.4-bcmath \
php7.4-raphf php7.4-xmlrpc 
```





# Code-Server

## 下载安装包

首先下载code-server安装包，网址为https://github.com/coder/code-server/releases。 选择对应的版本号，这里Debian使用的安装包是deb文件后缀，同时注意CPU的类型，amd64是amd的CPU，而arm64是intel的CPU，下载到本地。

上传安装包到Debian服务器上，可以通过SSH来进行上传,scp指令上传文件的方法如下：

```powershell
scp file username@hostname:/home/username
#将本地文件“file”上传到指定服务器的/home/username文件夹下
```

## 安装并设置

首先远程登录服务器并安装code-server

```powershell
ssh username@hostname

cd /home/username
dpkg -i code-server_4.20.0_amd64.deb
#-i是install安装的意思，记得修改对应的版本，保证文件名一样
```

然后设置code-server的设置文件，文件在root/.config/code-server/ 这个文件夹下，名叫config.yaml，如果没有找到这个文件夹或文件，可能是因为没有运行而没有产生设置文件，可以在终端输入code-server启动这个服务再ctrl+c中断掉，对应的设置文件就会产生。然后使用nano打开这个文件进行编辑，修改成如下的样子。

```yaml
bind-addr: 0.0.0.0:8080
auth: password
password: 密码
cert: false
```

其中0.0.0.0是广播地址，意味所有IP都可以连接这台机器的code-server服务，如果有需要可以自己改。将密码改为自己能记住的密码，在稍后登录时需要用到。

## 启动并登录

设置开机自启动并现在启动，由于code-server涉及根目录中文件的编辑上传，可以使用root账户进行登录，如果可以，建议设置一个其他账户进行登录。

```bash
systemctl enable --now code-server@root
```

这样，就开启了code-server服务。code-server服务器默认端口为8080，浏览器登录http:xxx.xxx.xxx.xxx:8080即可访问页面，输入密码即可进入code-server进行编辑。



# MariaDB（MySQL）

## 安装和配置

```bash
apt install mariadb-server
```



## 创建远程登陆用户

一般MariaDB不允许远程直接登录root账户，因此需要在本地创建一个账户用于登录远程MariaDB服务器。使用以下指令创建用户并授予权限，从而进行远程登陆。

```mysql
CREATE USER 'new_username'@'%' IDENTIFIED BY 'new_password';
# 创建用户，'%'表示允许从任何主机连接

GRANT ALL PRIVILEGES ON *.* TO 'new_username'@'%' WITH GRANT OPTION;
# 授予所有数据库的权限，*.*就是所有数据库，如果是某个数据库，则是"db_name.*"

FLUSH PRIVILEGES;
# 刷新权限
```

## 允许远程连接

### 允许从其他主机连接

MariaDB默认不允许远程连接，需要修改其设置文件才能进行远程连接。打开MariaDB的配置文件`my.cnf`，在Linux系统下通常位于`/etc/mysql/my.cnf`或者`/etc/my.cnf`。在设置文件中，找到`bind-address`一行，如果不存在，则可以手动添加一行。

```ini
bind-address = 0.0.0.0
```


其中0.0.0.0是广播IP，也就是允许其他所有主机连接至数据库。如果有需要可以自行更改。重启MariaDB服务使更改生效

```bash
systemctl restart mariadb
```

确保`bind-address`作为一个单独的选项，如果遇到报错，则需要将其放在[mysqld]之内。

```bash
root@Purgatory:/etc/mysql# mysql 
mysql: unknown variable 'bind-address=0.0.0.0
```

重新修改设置文件

```ini
[mysqld]
bind-address = 0.0.0.0
```

### 打开防火墙

允许从其他主机连接还需要打开相应的端口，MariaDB默认端口为3306，下面是利用`ufw`将其开启，如果没有相应防火墙设置可以跳过

```bash
ufw allow 3306
```



## 远程登录

在远程登录的设备终端，进行登录。

```bash
mysql -h <ip_address> -u <username> -p
```

然后会让你输入密码，确认后即登录到其数据库。



# FTP

## 下载vsftpd

```bash
apt install vsftpd
apt install ftp
```

## 设置账户

```bash
useradd -m -d /home/share/ -s /bin/bash ftp_user
# 创建一个以/home/share 为起始文件夹的用户ftp_user

passwd ftp_user
# 设置密码
```

## 设置vsftpd

- /etc/vsftpd.conf

  ```ini
  listen=NO
  allow_writeable_chroot=YES
  listen_ipv6=YES
  anonymous_enable=NO
  local_enable=YES
  write_enable=YES
  local_umask=022
  anon_upload_enable=NO
  anon_mkdir_write_enable=NO
  dirmessage_enable=YES
  use_localtime=YES
  xferlog_enable=YES
  connect_from_port_20=YES
  chroot_local_user=YES
  chroot_list_enable=YES
  chroot_list_file=/etc/vsftpd.chroot_list
  secure_chroot_dir=/var/run/vsftpd/empty
  pam_service_name=vsftpd
  rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
  rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
  ssl_enable=NO
  ```

- /etc/vsftpd.chroot_list

  ```ini
  ftp_user
  ```

## FTP服务器

```bash
systemctl restart vsftpd
# 重启FTP服务器使其生效

ftp ftp_user@localhost
# 连接至本地的FTP服务器
```

# FRP

## 配置frp服务器

```toml
# 绑定端口
bindPort = 7000

# 配置dashboard界面
webServer.addr = "0.0.0.0"
webServer.port = 7500
webServer.user = "admin"
webServer.password = "admin"
```



## 配置frp客户端

`frpc.toml`文件

```toml
serverAddr = "frp.arorms.cn"
serverPort = 7000
includes = ["./confd/*.toml"]
```

`confd`中两个文件

```toml
[[proxies]]
name = "cs2_tcp"
type = "tcp"
localIP = "127.0.0.1"
localPort = 27015
remotePort = 27015
```

```toml
[[proxies]]
name = "cs2_udp"
type = "udp"
localIP = "127.0.0.1"
localPort = 27015
remotePort = 27015

```

> [!CAUTION]
>
> 需要关闭服务器防火墙的绑定端口和隧道的远程端口，注意UDP和TCP模式。



## *StarryFrp*

下载软件

`/usr/local/bin/frpc`

守护进程配置文件

`/usr/lib/systemd/system/`

```ini
[Unit]
Description=StarryFrp Service
After=network.target

[Service]
Type=idle
User=nobody
Restart=on-failure
RestartSec=60s
ExecStart=/usr/local/bin/frpc -f %i

[Install]
WantedBy=multi-user.target
```





# MSTSC

## 安装

```bash
apt update
# 更新软件列表

apt install x-window-system-core gnome-core
# 安装gnome图形相关软件

apt install xrdp
# 安装xrdp
```

## 配置

1. `/etc/gdm3/daemon.conf`中，在`[security]`下增加一行`AllowRoot = true`
2. 修改`/etc/pam.d/gdm-password`文件，注释掉`auth required pam_succeed_if.so user != root quiet_success`

## 启动

```bash
init 6
```

## 禁止休眠

安装完图像操作系统后，系统会根据没有进行操作的时间而进入休眠以节省电源，常常导致各种服务和链接中断。

1. 查看休眠状态

   ```bash
   systemctl status sleep.target
   ```

2. 设置禁止休眠

   ```php
   systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
   ```

   
