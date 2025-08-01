202.195.167.230

test testest

**题目 1 新增 Linux 系统调用**

采用编译内核法，在 Linux 中增加一个系统调用

1. 系统调用实现的功能：计算一个数字的三次方
2. 另外写一个程序进行调用



**题目 2 实现基于模块的文件系统**

修改 ext3 或 ext4 的源代码，实现新的文件系统

1. 复制 ext3 或 ext4 的源代码，修改 makefile 文件，使用模块编译方法，重新编译 Linux 内核。
2. 可以动态加载或卸载新的文件系统。
3. 至少需要修改文件系统的名称，最好能对文件写操作向系统后台打印出信息。



**题目 3 新增 Linux 驱动程序**

增加一个驱动程序（使用内存模拟设备），使用模块编译方法。

1. 可以动态加载和卸载新的驱动。
2. 通过程序或命令行使用该驱动。
3. 至少能通过该驱动保存 256MB 数据，还能将这些数据读取出来。
4. 重新编译 Linux 内核，可以模仿 ramdisk 的实现方法。



**题目 4 统计 Linux 系统缺页的次数**

通过在 Linux 内核中自建变量，并利用 `/proc` 文件系统作为中介的方法，统计系统缺页的次数。

1. 在内核中实现缺页次数统计。
2. 编译并安装新的内核。
3. 新建内核模块，并加载到新内核，通过 `/proc` 实现用户态下查看缺页次数。



**题目 5 进程/线程通信**

利用进程/线程间通信编写程序实现阅览室问题，实现多个读者进程注册、阅读、注销的过程，假设阅览室共有五个座位。

1. 使用信号量机制和共享存储区机制实现多个进程/线程之间的通信，同时实现注册与注销的互斥操作。
2. 注册操作要求读者进程填写个人手机或其他身份信息；注销操作要求读者撤销填写的个人信息。