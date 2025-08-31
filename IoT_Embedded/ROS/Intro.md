---
title: ROS 基本教程
date: 2025-03-10
author: Holmes Amzish
tags: ['robot']
---

# ROS 基本介绍

ROS 官网 https://www.ros.org/

# ROS 安装

## 版本说明

ROS 存在众多版本，由于贴合 Ubuntu 系统的更新，基本上每一个 Ubuntu 的长期支持版本（LTS）都会有对应的 ROS 版本，以下是几个常见的 ROS 版本：

| ROS Version            | Ubuntu Version   |
| ---------------------- | ---------------- |
| ROS 2 Jazzy Jalisco    | Ubuntu 24.04 LTS |
| ROS 2 Humble Hawksbill | Ubuntu 22.04 LTS |

由于现在（2025-03-10）对 Ubuntu 22.04 LTS 的支持要更加完善，所以本文以 ROS Humble 为例。其次，假设使用的 shell 是 zsh。

## 安装步骤

以下是大致步骤和基本翻译，详情可以访问原网站 https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html

### 设置本地环境

确定本地环境支持 UTF-8 编码

```bash
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```

### 设置软件源

首先要添加 ROS2 apt 软件源到当前系统中

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

添加 ROS 2 GPG key

```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

添加库到软件源列表

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

### 安装 ROS 2 包

更新软件源

```bash
sudo apt update
sudo apt upgrade
```

安装 ROS 2 桌面

```bash
sudo apt install ros-humble-desktop
```

安装 ROS-Base（通信库与消息包、命令行工具等）

```bash
sudo apt install ros-humble-ros-base
```

安装 ROS 开发工具

```bash
sudo apt install ros-dev-tools
```

### 环境设置

在每次启动终端时初始化，可以通过手动加载初始化脚本

```bash
# Replace ".bash" with your shell if you're not using bash
# Possible values are: setup.bash, setup.sh, setup.zsh
# [注意] 按照官方英文提示，替换成当前使用的 shell
source /opt/ros/humble/setup.bash
```

或者将本行添加到 shell 初始化脚本中，zsh 的初始化脚本为 `~/.zshrc`



## 运行示例

### Talker-listener

安装完 `ros-humble-desktop` 后，既可以尝试一些例子。下面的示例中已经将 ros 初始化脚本添加到默认启动。

在终端中，加载安装脚本并运行一个 C++ 程序 `talker`，此程序会不断发布消息 “Hello World"。

```bash
ros2 run demo_nodes_cpp talker
```

然后在另一个终端中运行一个 Python 程序 `listener`

```bash
ros2 run demo_nodes_py listener
```

可以看到在 talker 发送消息后，listener 会监听到消息。







# ROS 包

ROS 资源入口：https://index.ros.org/

## 包的下载

首先可以在 资源入口中筛选版本和查看包的详细信息，然后根据描述下载。

```bash
sudo apt install ros-<version>-<package>

# 下载 rqt_robot_steering
sudo apt install ros-humble-rqt-robot-steering
```



## 运行

```bash
rosrun rqt-robot-steering rqt-robot-steering
```

