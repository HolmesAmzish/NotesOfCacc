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

- 修改密码

```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
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

# 示例

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
