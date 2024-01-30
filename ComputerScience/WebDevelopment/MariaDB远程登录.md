# MariaDB 远程登陆

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