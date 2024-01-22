# 在Debian系统安装LAMP环境
LAMP即Linux，Apache，Mysql，php

## 安装Apache
```bash
apt update
apt install apache2
```



通过systemctl查看apache是否运行，也可以通过第二行手动设置开机自启动
```bash
systemctl status apache2
systemctl enable --now apache2
```



## 安装PHP环境
在安装PHP同时，使用apache为web服务器运行PHP程序，使用mysql作为数据库，所以也要安装php的apache和mysql模块。
```bash
apt install php libapache2-mod-php php-mysql
```



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

