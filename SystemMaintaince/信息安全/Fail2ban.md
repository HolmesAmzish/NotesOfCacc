# fail2ban

## 基本介绍

Fail2ban 是一个根据日志判断恶意流量自动管理封禁 IP 连接的服务。其工作在应用层以避免对服务器网络的更改，同时对应用日志能更加准确的判断出恶意流量。用户也可以自定义过滤器来对自己的应用创建基本的防护。

**下载**

```bash
sudo apt update
sudo apt install fail2ban -y
```

**基本设置**

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

```bash
fail2ban-client reload    # 重新加载
fail2ban-client status <jail_name>
fail2ban-client set <jail_name> unbanip <ip_address>
```

## 监狱 jail.d

## 过滤器 filter.d

`/etc/fail2ban/filter.d/frp-ssh.toml`

```toml
[Definition]
failregex = \[talos-ssh\] get a user connection \[(<HOST>\d+\.\d+\.\d+\.\d+):\d+\]
ignoreregex =
```
