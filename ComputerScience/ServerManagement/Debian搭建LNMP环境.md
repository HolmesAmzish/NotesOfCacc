# 在Debian系统安装LNMP环境
LAMP即Linux，Apache，Mysql，php

## 安装Apache
```bash
apt update
apt install nginx
```

通过systemctl查看apache是否运行，也可以通过第二行手动设置开机自启动
```bash
systemctl status nginx
systemctl enable --now nginx
```



## 安装和配置PHP环境

首先安装PHP

```bash
apt install php7.4
```

在安装PHP同时，还要安装好必要包。
```bash
apt install php7.4-fpm php7.4-cgi php7.4-curl php7.4-gd php7.4-xml php7.4-xmlrpc php7.4-mysql php7.4-bz2
```

然后配置PHP环境，到/etc/nginx/sites-available/文件夹中，修改default。这是nginx的主配置文件，如果一台服务器包含了多个网站，则配置文件需要去conf文件夹修改。此处修改主要是将php服务的内容注释给去掉，使php生效

![php](/img/16.png)



## 检查php是否安装成功

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



## 安装MariaDB

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

