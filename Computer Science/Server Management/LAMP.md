# LAMP

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
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        ServerName dev.val.arorms.cn

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/val.arorms.cn

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
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

然后配置PHP环境，到/etc/nginx/sites-available/文件夹中，修改default。这是nginx的主配置文件，如果一台服务器包含了多个网站，则配置文件需要去conf文件夹修改。此处修改主要是将php服务的内容注释给去掉，使php生效

![php](C:/Users/Holme/OneDrive/Document/img/16.png)



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

