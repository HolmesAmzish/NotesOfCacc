# Debian 建立 SSH 连接
## 安装 SSH 服务器

Debian 默认安装了SSH服务器，如果发现系统没有安装过SSH，可以手动下载。

```bash
apt update
# 更新应用列表

apt install -y openssh-server
# 下载SSH服务器
```

## 检查和启用 SSH 服务器

```bash
systemctl status ssh
# 检查SSH服务器是否开启

systemctl enable --now ssh
# 手动设置SSH开机自启动和现在启动
```

还有其他选项用来手动设置SSH服务

```bash
system [option] ssh
```

| 选项    | 操作              |
| ------- | ----------------- |
| start   | 启动SSH           |
| stop    | 停止SSH           |
| enable  | 开机允许SSH自启动 |
| disable | 开机禁止SSH自启动 |
| restart | 重启SSH服务       |

*详情查看systemctl指令详细说明*

## 访问 SSH 服务器

首先在本地查询其IP，两个命令都可以显示IP

```bash
hostname -I
# 查询局域网IP

ip address
# 查询网卡信息
```

返回你的电脑，连接 Debian 的 SSH 服务器

```powershell
ssh username@ip-addr
# 以username 的身份登录 ip-addr
```

然后输入 yes 确认指纹，随后输入 username 的密码登录到 Debian 的 SSH 服务器

操作结束后，可以通过 exit 命令退出 SSH 服务器返回本地的命令行。

```bash
exit
```



## 启用 SSH 远程 root 登录权限

SSH远程连接时可能无法直接通过root账户登录，会显示权限不足（Permission denied, please try again.）要开启root账户远程登录，找到`/etc/ssh/sshd_config` 文件并修改其中的设置，需要找到这两个设置并将参数修改为`yes`。

```bash
nano /etc/ssh/sshd_config
# 以nano打开sshd_config设置文件
```

```
PermitRootLogin yes
# 允许远程root登录

PasswordAuthentication yes
# 开启密码认证
```
![rootpermit](/img/13.png)

然后重启ssh服务器，使其设置生效。

```bash
systemctl restart ssh
```

## 修改 SSH 服务端口

SSH 服务的默认端口为 22，如果你想要修改 SSH 服务的端口，还是前往SSH的设置文件（sshd_config）并修改他，将 port 一行的井号删除使其生效，并修改其参数22为你想要的端口。

![port](/img/14.png)

最后重启 SSH 服务即可生效。
