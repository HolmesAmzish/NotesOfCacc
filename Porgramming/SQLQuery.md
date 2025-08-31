---
title: SQL Query
date: 2025-07-13
author: Cacciatore
---



Sort

```sql
SELECT * FROM <table> ORDER BY <column> DESC;
```



Page

```sql
SELECT *
FROM <table>
ORDER BY <column> DESC
LIMIT <page_size> OFFSET <page_offset>;
```





```sql
SELECT COUNT(*) FROM <table_name>;

SELECT AVG(age) average FROM user WHERE gender = 'F';
```





```sql
SELECT
u.id user_id,
u.username username,
g.id group_id,
g.groupname groupname
FROM users u, groups, g;
```



```sql
SELECT e.Id, e.EmployeeName, e.DepartmentId
FROM Employee
INNER JOIN Department d
ON e.DeparmentId = d
```



