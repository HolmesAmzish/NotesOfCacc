---
title: 虚拟内存
date: 2025-04-06
author: Holmes Amzish
---



# 虚拟内存的概念

**虚拟内存**（英语：Virtual memory）是计算机系统内存管理的一种技术。它使得应用程序认为它拥有连续可用的内存（一个连续完整的地址空间），而实际上[物理内存](https://zh.wikipedia.org/wiki/物理内存)通常被分隔成多个[内存碎片](https://zh.wikipedia.org/wiki/碎片化)，还有部分暂时存储在外部磁盘存储器上，在需要时进行数据交换。与没有使用虚拟内存技术的系统相比，使用这种技术使得大型程序的编写变得更容易，对真正的物理内存（例如[RAM](https://zh.wikipedia.org/wiki/隨機存取記憶體)）的使用也更有效率。此外，虚拟内存技术可以使多个[进程](https://zh.wikipedia.org/wiki/行程)共享同一个[运行库](https://zh.wikipedia.org/wiki/函式庫)，并通过分割不同进程的内存空间来提高系统的安全性。

**交换内存**是 Unix 系统对虚拟内存的一种实现方式，具体指磁盘上的一块专用区域（称为“交换分区”或“交换文件”），用来临时存储从物理内存中移出的数据。当物理内存（RAM）不足时，操作系统会将一部分不活跃的内存页面（数据块）写入交换内存中，释放RAM给更紧急的任务。当程序需要这些数据时，操作系统再从交换内存中把数据读回RAM。这种机制通常被称为“页面交换”（Swapping）。而在 Windows 中称为**页面文件（Page File）**。

一般来说，分配交换内存应该设置为内存的 1 ～ 2 倍，比如 16G 内存可以分配差不多 16G 交换内存。

# 虚拟内存的更改

## Linux 系统中交换内存的更改

在 Ubuntu 系统中，交换内存（Swap Memory）可以通过创建或调整“交换分区”（Swap Partition）或“交换文件”（Swap File）来实现。

在调整之前，可以先检查系统当前的交换内存状态：

```bash
swapon --show
```

```
NAME      TYPE  SIZE  USED PRIO
/swapfile file  2G    0B   -2
```

也可以通过查看设备的内存使用情况来查看交换内存的状态：

```bash
free -h
```

禁用当前交换文件：

```bash
sudo swapoff /swapfile
sudo rm /swapfile
```

创建新的交换文件

```bash
sudo fallocate -l 16G /swapfile
sudo chmod 600 /swapfile
```

格式化为交换文件

```bash
sudo mkswap /swapfile
```

启用新的交换文件

```bash
sudo swapon /swapfile
swapon --show
```

确认永久生效

```bash
sudo vim /etc/fstab
```

确认有如下行，一般来说如果之前删除没有进行别的操作，这里还会留着之前的信息不用更改。

```ini
/swapfile none swap sw 0 0
```

