---
title: ddns-go 动态域名解析
date: 2025-02-26 16:44
---

# 什么是 DDNS

**DNS（域名系统）** 是互联网的电话簿，将易于记忆的域名（如 `www.example.com`）转换为计算机可以理解的 IP 地址（如 `192.0.2.1`）。这使得用户无需记住复杂的数字地址即可访问网站。



**DDNS（动态域名服务，Dynamic DNS）** 是对传统 DNS 的扩展，旨在解决 IP 地址频繁变化的问题。在某些网络环境中，设备的公网 IP 地址可能会动态变化，导致固定的域名无法始终指向正确的 IP 地址。DDNS 通过自动更新域名与 IP 地址的映射关系，确保即使 IP 地址发生变化，用户仍然可以通过固定的域名访问设备或服务。 



**DNS 和 DDNS 的主要区别**：

- **IP 地址类型**：DNS 主要用于处理静态 IP 地址，即 IP 地址不会频繁变化的情况。而 DDNS 适用于动态 IP 地址，即 IP 地址可能会频繁变化的情况。 

- **更新机制**：DNS 的记录通常是静态的，需要手动更新。而 DDNS 能够自动检测 IP 地址的变化，并实时更新域名解析记录。 

- **应用场景**：DNS 适用于服务器等固定 IP 地址的设备。而 DDNS 适用于家庭网络、移动设备等 IP 地址可能变化的环境。 

  

# DDNS-GO 的安装

**DDNS-GO** 是一项开源软件，在 github 上地址为 https://github.com/jeessy2/ddns-go 。下载对应的发布版本，本教程以 Linux 系统（Ubuntu）为例。

## 安装 ddns-go

首先解压程序

```bash
tar -xzvf filename.tar.gz
```

执行安装程序

```bash
sudo ./ddns-go -s install
```

## 配置与启动

启动 ddns-go

```bash
./ddns-go
```

ddns-go 提供了一个 webui 来进行图形化操作，要访问 ddns-go 的 web 界面，地址在 `http://localhost:9876`。在浏览器中访问该地址即可进行配置。

> [!TIP]
>
> 如果目标机器不在局域网内且没有公网没那么方便直接访问没有穿透的端口，假设之前已经设置过 ssh 端口的内网穿透，可以通过 ssh 隧道进行连接：
>
> ```bash
> ssh -L 8080:localhost:9876 <username>@<remote-machine> -p <port>
> # 将远程主机的目标端口绑定到本地端口上，也就是接下来浏览器访问地址为 http://localhost:8080
> ```
>
> 这样远程主机的 localhost:9876 就被转发到自己主机的 localhost:8080 了，对于远程主机的其他目标也适用。



## 设置动态域名解析

以阿里云为例，需要在阿里云创建一个 `AccessKey` 来提供用户的操作权限，并设置一个名下的域名，程序就会根据域名的变化来与域名供应商进行比对并更新。

点击保存即可完成设置。



# DDNS-GO 的其他设置

## 守护进程

如果需要设置开机自启动，在 Linux 中可以直接设置守护进程来控制程序的是否自启动和状态，在 `/etc/systemd/system` 中创建并设置 `ddns_go.service`：

```ini
[Unit]
Description=DDNS-GO Service
After=network.target

[Service]
ExecStart=/path/to/ddns-go
Restart=always
User=your_username
Group=your_group

[Install]
WantedBy=multi-user.target
```

然后重新加载 `systemd` 设置并重新启动

```bash
sudo systemctl daemon-reload
sudo systemctl enable ddns-go.service
sudo systemctl start ddns-go.service
```

## 更新时间

在 **动态域名服务（DDNS）** 中，**TTL（生存时间）** 是指 DNS 记录在缓存中保存的时间长度，单位通常为秒。

TTL 值的设置需要在 **更新频率** 和 **服务器负载** 之间找到平衡。

较长的 TTL 值（如 1 小时）可以减少 DNS 查询次数，降低服务器负载，但可能导致 IP 地址变化后，全球范围内的 DNS 缓存需要更长时间才能更新，影响访问的及时性。

相反，较短的 TTL 值可以使 DNS 记录更快地传播更新，但会增加对 DNS 服务器的查询频率，可能导致服务器负载增加。
