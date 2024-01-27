# MariaDB

## 基本操作

```bash
mysql -u<username> -p<password>
# Login MariaDB Server

exit
# Exit from Server
```

```bash
create user 'dvwa'@'localhost' identified by 'dvwa';

grant all on *.* to 'dvwa'@'localhost';

set password for 'dvwa'@'localhost' = password('dvwa');
```