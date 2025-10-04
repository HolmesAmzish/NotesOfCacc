---
title: postgresql
date: 2025-07-12
---

Install

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

This installs the PostgreSQL server and some useful utilities. The service starts automatically

Then you need to login postgres user to do operations

```bash
sudo -i -u postgres  # This will switch you into postgres user
```

Then enter the postgresql shell

```bash
psql
```

Here's basic operation commands.

Change password

```postgresql
\password postgres
```

*You can also change password by sql command*

```sql
ALTER USER postgres PASSWORD 'your_secure_password';
```

Database command

```bash
\l
\list  # List all database
\c <database_name> # Connect(use) database
\dt  # Display all the table
\d <table_name> # Describe the table
\du
\dn
\dp
\q  # Quit
\?  # Help
```



