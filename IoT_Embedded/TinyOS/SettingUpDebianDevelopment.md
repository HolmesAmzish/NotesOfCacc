---
title: Setting Up Debian Development
date: 2025-04-01
author: Holmes Amzish
tags: ['embedded']
---

# 在 Deb 系 Linux 系统上安装开发环境

仅 Linux，特别是 Debian 系发行版，比如 Debian 本身和 Ubuntu。

其中 Ubuntu 16.04 和 Ubuntu 18.04 已经被测试过了

## 安装环境

首先在 Ubuntu 和 TinyOS 官网上下载 ISO 镜像，并装载到可以启动媒体，比如 USB 和 DVD。也可以通过 grub 在以有的 Linux 系统上安装。

这里使用 Debian 9 stretch 安装，因为此版本是的TinyOS 最后一个明确支持的 Linux 版本。由于 stretch 现在也已经在 2022 年停止维护，软件源和代理也已经全部移至归档仓库，在安装时不管 apt 源报错，安装完成后需要手动添加归档仓库。

当系统安装完成，启动系统，首先需要更改软件源：

```bash
su # 提权
nano /etc/apt/source.list
```

将原来内容注释，并添加两个阿里云镜像：

```ini
deb http://mirrors.aliyun.com/debian-archive/debian stretch main contrib non-free
deb http://mirrors.aliyun.com/debian-archive/debian-security stretch/updates main contrib non-free
```

然后运行 `apt update` 更新软件包列表。



并使用 Debian 系的包管理器（apt）安装下面包：

```bash
sudo apt install build-essential stow automake autoconf libtool libc6-dev git-core git-daemon-run git-doc git-email git-gui gitk gitmagic openssh-client openssh-server graphviz

sudo apt install python3 python3-serial python python-serial
```

>[!NOTE]
>
>Debian 上的 TinyOS 工具包在斯坦佛和 TinyProd.net 的源可用，斯坦佛已经不再维护。在 TinyProd.net 的工具链仍然在更新（2019-05-29）。

## 安装工具链

### 设置仓库权限

首先需要设置 `dpkg` 和 `apt` 中 tinyprod 工具仓库的位置。

将TinyProd工具链的仓库添加到APT源列表中：

```bash
# 将TinyProd的仓库签名密钥添加到APT密钥链中，必要时验证仓库
wget -O - http://tinyprod.net/repos/debian/tinyprod.key | sudo apt-key add -
```

然后将仓库添加到 APT 源中

```bash
sudo echo "deb http://tinyprod.net/repos/debian stretch   main" >> /etc/apt/sources.list.d/tinyprod-debian.list
sudo apt update
```

### 安装基本工具

```bash
sudo apt install nesc tinyos-tools-devel
```



## 