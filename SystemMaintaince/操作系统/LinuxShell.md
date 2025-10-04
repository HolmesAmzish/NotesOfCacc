# 文件和目录操作类

## ls 查看本目录

```bash
ls 
# 查看本目录
```

详细语法`ls [alertAFR] [name]`

- -a 显示所有文件及目录（包括隐藏目录）
- -d 只列出目录
- -l 以长格式显示文件和目录信息
- -v 进行自然数排序
- -r 倒序显示文件和目录
- -t 将按照修改时间排序，最新的文件在最前面
- -A 同-a，但是不列出当前目录和父目录`.`和`..`
- -F 在列出的文件名称后添加某个符号
- -R 递归显示目录中所有文件和子目录

## cat 查看文件

```bash
cat file
# 查看文件

tac file
# 倒过来查看文件
```

## vim 编辑和查看文件

使用Vim来编辑文件。Vim是在Vi只能在Unix系统上运行而为Linux而写的编辑软件，功能强大，为命令行模式提供一个高效的操作界面。

```vim
vim file
# 使用vim打开文件
```

输入`I`进入插入模式，编辑完成后按下`esc`返回命令模式，输入`:wq`保存并退出。

或者使用nano来编辑文件，nano是一款后期的软件，提供了更优的编辑界面和比较常用的快捷键

```bash
nano file
# 使用nano打开文件
```

`ctrl + s`保存， `ctrl + x`退出。

查看文件，使用cat来查看文件。

## find 查找文件

```bash
find /path -name "filename"
```

## grep 筛选信息

```bash
ls | grep 2024
# 筛选含有字符串，2024的信息。
```



## xargs 参数输出

```bash
cat example.txt | xargs

cat example.txt | xargs -n 3

# Split by "X"
cat example.txt | xargs -d X
```

## tr 转换

```bash
# Transform uppercase to lowercass
echo "HELLO WORLD!" | tr 'A-Z' 'a-z'

# Transform tab to space
tr '\t' ' ' < file.txt

# Delete all number
echo "Hello 123 world 456" | tr -d '0-9'
```



# 流处理





# 下载和解压

## tar 归档

```bash
tar -cvf file.tar /path/to/folder
# 压缩
```

```bash
tar -zxf /path/to/tar_file
# 解压
```

## unzip 解压

```bash
unzip zip_file -d /path/to/destination/
```

## gz

```bash
gzip -d /path/to/gz_file
```



# 信息安全

## 单向散列算法

```bash
# Calculate the md5 code
md5sum filename > file_sum.md5

sha1sum filename
```

http://codahale.com/how-to-saftylystore-a-password/

## crypt

```bash
# Encrypt file
crypt < input_file > output_file

crypt PASSPHRASE < input_file > encrypted_file

# Decrypt file
crypt PASSPHRASE -d < encrypted_file > output_file
```



## gpg

```bash
gpg -c filename

gpg filename.gpg
```



## base64

```bash
base64 filename > outputfile

base64 -d file > outputfile
```





# 软件和服务类

## apt 下载

```bash
apt update
# 更新列表

apt upgrade
# 更新软件

apt install application
# 安装软件

apt remove application
# 卸载软件
```

## dpkg

```bash
# 安装软件包
dpkg -i package.deb

# 列出所有软件包
dpkg -l

# 移除软件
dpkg -r package_name

# 彻底删除软件，包括设置
dpkg --purge package_name
```





## systemctl 服务

```bash
systemctl status service
# 查看服务状态

systemctl start service
# 启用服务

systemctl enable --now service
# 设置服务开机自启动，并且现在生效

systemctl disable --now serivce

systemctl stop service
# 停止服务
```

## gz 本地安装

```bash
tar -zxvf filename.gz
```

## screen 窗口

```bash
screen -ls # 查看所有窗口
screen -S screenName # 创建一个名为screenName的窗口
screen -r screenName # 回到screenName窗口
```

`crtl + a + d`返回主终端
`crtl + d`删除当前窗口



# 系统管理

## du 查看文件大小

```bash
du -sh
# 查看本目录的大小

du * -sh
# 查看子目录大小
```



## lsusb 查看usb接口

```bash
lsusb
```



## lsblk 查看硬盘设备

List block

```bash
lsblk
```



df 查看硬盘

```bash
df -h
# 列出所有硬盘信息
```



## mount 挂载

```bash
mount /dev/sdx1 /mnt/usb
# 将设备挂载到挂载点

umount /mnt/usb
# 取消挂载点的挂载
```



## hostname 主机名

```bash
hostname
# 显示主机名

hotnamectl
# 显示主机名的详细信息

hostnamectl set-hostname <name>
# 更改主机名
```



## ssh SSH连接

```bash
ssh username@hostname
# 以username的身份连接到hostname

ssh username@hostname -p port
# 以port端口号连接
```

# 网络

## ping

```bash
ping target

ping -s 1300 target
# 向目标发送1300字节的数据包

ping -s 1300 -f target
# 
```

## hping3

```bash
hping3 -S -V --flood target
# hitting the port 80 server of server
```

## nmap

```bash
nmap -O -Pn target
# scan the OS of target

nmap -A target
# default script scanning from nmap and trace route
```

## iftop

```bash
iftop
# 监测网卡流量

iftop -i wlo1
# 监测特定网卡的流量
```

## curl HTTP请求

```
curl http://localhost/weather/getB
```



# 其他

## script

```bash
script -t 2> timing.log -a output.session

type some commands...

exit
```





## history

```bash
history # 查看历史命令
```



## alias 定义命令

```bash
alias short="command"
```

