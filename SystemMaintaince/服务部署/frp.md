---
title: frp
date: 2025-02-25 13:37
tags: ['servcer']
---

# frp 内网穿透

FRP是一款高性能的反向代理应用，专注于内网穿透。在今天IPv4地址非常紧张的情况下，可以选择使用内网穿透将一些内网服务器的程序或者说项目部署，允许公网访问。他需要一个用来转发流量的公网服务器，仅仅用来转发流量，通常可以使用阿里云，华为云一类的云服务器，且配置要求很低，只需要考虑网络带宽问题，租金会比较便宜。

## 通用

### 配置校验

```bash
frpc/s verify -c ./frp.toml
```

### 拆分配置

通过 `includes` 参数可以在主配置中包含其他配置文件

```toml
# frpc.toml
serverAddr = "x.x.x.x"
serverPort = 7000
includes = ["./confd/*.toml"]
```

```toml
# ./confd/test.toml
[[proxies]]
name = "ssh"
type = "tcp"
localIP = "127.0.0.1"
localPort = 22
remotePort = 6000
```

## frps 服务端

### 服务器设置

首先需要下载frp软件，进入github页面https://github.com/fatedier/frp，随后到Releases处可以下载相对应的系统版本。

将frp程序下载后，会有四个主要的文件，其中服务器需要用到的是`frps`和`frps.toml`，前者是内网穿透服务器程序，后者则是设置文件。编辑设置文件后写入以下内容。

```toml
bindPort = 7000                          # 服务器监听端口，默认7000
auth.token = "123456"                        # 服务器token，用来防止盗用

webServer.addr = "0.0.0.0"            # 网页控制面板监听地址，默认0.0.0.0
webServer.port = 7500                  # 网页控制面板监听端口
webServer.user = "admin"              # 控制面板用户名
webServer.password = "admin"          # 控制面板密码
```

### 运行

运行服务器程序就可开启服务端，也可以自己设置一个开机自启动。

```bash
./frps -c ./frps.toml
```

如果需要查看服务器隧道的情况，可以浏览器访问服务器地址加上设置的7500端口（xxx.xxx.xxx.xxx:7500)，输入用户名和密码后即可进入dashboard查看总体的信息。

如果需要后台运行，或者开机自启动，可以设置守护进程（daemon），在 `/etc/systemd/system/` 文件夹下创建并编辑 `frps.service`，然后启动。

```ini
[Unit]
Description=FRP Server Service
After=network.target

[Service]
Type=simple
User=nobody 
ExecStart=/opt/frp_0.61.1_linux_amd64/frps -c /opt/frp_0.61.1_linux_amd64/frps.toml
Restart=on-failure
RestartSec=5s
KillMode=process

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl start frps

# 设置开机自启动并现在启动
sudo systemctl enable --now frps
```

> [!TIP]
> 
> 如果需要开放 1-1023 端口，这一部分需要更大权限，比如需要 root 账户进行，可以将 User=nobody 一行删除或注释。

## frpc 客户端

而客户端则同样需要执行程序和设置，分别是`frpc`和`frpc.toml`，下面是以ssh设置为例子。

### TCP & UDP

```toml
serverAddr = "xxx.xxx.xxx.xxx"        # 服务器地址
serverPort = 7000                    # 服务器端口
auth.token = "123456"                        # 服务器token，与设置一样

[[proxies]]
name = "ssh"                        # 代理服务名称
type = "tcp"                        # 代理类型
localIP = "127.0.0.1"                # 代理地址
localPort = 22                        # 代理本地端口
remotePort = 6000                    # 远程开放端口
```

### HTTP

设置 **http** 配置文件，内网穿透还允许自定义域名进行连接，通过指定customDomains来远程访问时进行不同域名访问。记住域名解析需要指向公网服务器。

```toml
# ./confd/http.toml
[[proxies]]
name = "http"
type = "http"
localIP = "127.0.0.1"
localPort = 80
customDomains = ["www.example.com"]
```

服务器也需要设置相应端口，在 `frps.toml` 设置添加一行：

```ini
vhostHTTPPort = 80
```

这是设置服务器将 80 端口作为 frps 程序的 http 

此处在运行时，还需要将 www.example.com 记录指向服务器地址，然后在浏览器输入域名即可通过内网穿透服务器访问到本地服务器的 web 内容。

### 运行

随后开启客户端程序即可

```bash
./frpc -c ./frpc.toml
```

同理，客户端也可以启动守护进程

```ini
[Unit]
Description=FRP Client Service
After=network.target

[Service]
Type=simple
User=nobody 
ExecStart=/opt/frp_0.61.1_linux_amd64/frpc -c /opt/frp_0.61.1_linux_amd64/frpc.toml
Restart=on-failure
RestartSec=5s
KillMode=process

[Install]
WantedBy=multi-user.target
```

> [!NOTE]
> 
> 在客户端填写服务器地址时，可以使用域名，但是域名需要备案才能连接。
