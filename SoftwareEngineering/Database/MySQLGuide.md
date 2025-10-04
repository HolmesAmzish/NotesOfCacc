---
title: MySQL 软件操作指南
author: Cacciatore
date: 2025-07-03
status: posted
category: document
tags: ['mysql', 'database']
---

# 安装与配置

## 安装

```bash
sudo apt update
sudo apt install mysql-server  # Install mysql server
```

MySQL 配置文件路径：`/etc/mysql/my.cnf`

## 服务管理

```bash
sudo systemctl start mysql
sudo systemctl stop mysql
sudo systemctl restart mysql
```

设置为开机启动

```bash
sudo systemctl enable --now mysql
```

# 用户与权限管理

**创建用户**

```sql
-- Create local user
CREATE USER 'local_user'@'localhost' IDENTIFIED BY 'password';

-- Create remote access user
CREATE USER 'remote_user'@'%' IDENTIFIED BY 'P@ssw0rd';
```

**修改密码**

```sql
ALTER USER 'user'@'localhost' IDENTIFIED by 'newpassword'
```

**授权与撤销权限**

```sql
-- Give all the privileges
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
```

# 数据库操作
