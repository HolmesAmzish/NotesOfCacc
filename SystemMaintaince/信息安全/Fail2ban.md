```bash
sudo apt update
sudo apt install fail2ban -y
```

```bash
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo nvim /etc/fail2ban/jail.local
```

设置开启 SSH 监控

```properties
[sshd]
enabled = true
port = ssh
logpath = %(sshd_log)s
maxretry = 5
bantime = 3600
findtime = 600
```

