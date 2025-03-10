# MySQL 基础操作指南

## 1. 登录与退出

```bash
mysql -u <username> -h <address> -p
# 登录 MySQL 服务器

exit
# 退出 MySQL
```

## 2. 用户管理

### 2.1 创建用户

```mysql
CREATE USER 'new_user'@'%' IDENTIFIED BY 'new_password';
# '%' 允许从任何主机连接
```

### 2.2 设置/修改密码

```mysql
SET PASSWORD FOR 'username'@'localhost' = PASSWORD('new_password');
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
```

### 2.3 授权用户权限

```mysql
GRANT ALL PRIVILEGES ON *.* TO 'username'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES; # 刷新权限
```

### 2.4 删除用户

```mysql
DROP USER 'username'@'%';
```

### 2.5 允许连接

在 MariaDB 中，修改如下文件 `/etc/mysql/mariadb.conf.d/50-server.cnf`

```ini
bind-address = 0.0.0.0
# 将 127.0.0.1 改为 0.0.0.0 即为允许全部主机建立连接
```





## 3. 数据库操作

### 3.1 创建数据库

```mysql
CREATE DATABASE <db_name> DEFAULT CHARACTER SET utf8mb4;
```

### 3.2 查看数据库

```mysql
SHOW DATABASES;
SHOW CREATE DATABASE <db_name> \G;
```

### 3.3 删除数据库

```mysql
DROP DATABASE <db_name>;
```

### 3.4 选择数据库

```mysql
USE <db_name>;
SELECT DATABASE(); # 查询当前数据库
```

## 4. 数据表操作

### 4.1 查看数据表

```mysql
SHOW TABLES;
DESCRIBE <table_name>;
```

### 4.2 创建数据表

```mysql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    gender CHAR(1),
    birthday DATE,
    department VARCHAR(50)
) DEFAULT CHARSET=utf8mb4;
```

### 4.3 修改表结构

```mysql
ALTER TABLE table_name ADD COLUMN new_column_name datatype;
ALTER TABLE table_name DROP COLUMN column_name;
```

### 4.4 删除数据表

```mysql
DROP TABLE <table_name>;
```

## 5. 数据操作

### 5.1 插入数据

```mysql
INSERT INTO users (username, password, gender) VALUES
('alice', 'password1', 'F'),
('bob', 'password2', 'M');
```

### 5.2 查询数据

```mysql
SELECT * FROM users;
SELECT name, gender FROM users WHERE id = 1;
```

### 5.3 更新数据

```mysql
UPDATE users SET gender = 'female' WHERE id = 2;
```

### 5.4 删除数据

```mysql
DELETE FROM users WHERE id = 1;
DELETE FROM users; # 删除所有数据
TRUNCATE TABLE users; # 清空表并重置自增 ID
```

## 6. 数据库备份与恢复

### 6.1 导出数据库

```bash
mysqldump -u 用户名 -p 数据库名 > backup.sql
```

### 6.2 导入数据库

```bash
mysql -u 用户名 -p 新数据库名 < backup.sql
```

## 7. MySQL 存储引擎

```mysql
SHOW ENGINES;
```

## 8. MySQL 数据类型

### 8.1 整数类型

| 类型      | 取值范围（无符号） | 字节数 |
| --------- | ------------------ | ------ |
| TINYINT   | 0~255              | 1      |
| SMALLINT  | 0~65535            | 2      |
| MEDIUMINT | 0~16777215         | 3      |
| INT       | 0~4294967295       | 4      |
| BIGINT    | 0~2^64-1           | 8      |

### 8.2 浮点数类型

| 类型         | 字节数 |
| ------------ | ------ |
| FLOAT        | 4      |
| DOUBLE       | 8      |
| DECIMAL(M,D) | 变长   |

### 8.3 日期时间类型

| 类型      | 格式                | 说明        |
| --------- | ------------------- | ----------- |
| DATE      | YYYY-MM-DD          | 日期        |
| TIME      | HH:MM:SS            | 时间        |
| YEAR      | YYYY                | 年份        |
| DATETIME  | YYYY-MM-DD HH:MM:SS | 日期时间    |
| TIMESTAMP | YYYY-MM-DD HH:MM:SS | UNIX 时间戳 |

### 8.4 字符串类型

| 类型       | 说明     |
| ---------- | -------- |
| CHAR(M)    | 固定长度 |
| VARCHAR(M) | 变长     |
| TEXT       | 文本数据 |

------

## 示例：创建用户表并插入数据

```mysql
CREATE DATABASE test_data;
USE test_data;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    gender CHAR(1)
);

INSERT INTO users (username, password, gender) VALUES
('alice', 'password1', 'F'),
('bob', 'password2', 'M'),
('charlie', 'password3', NULL);
```
