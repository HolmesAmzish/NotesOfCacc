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

Change password

```postgresql
\password postgres
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



