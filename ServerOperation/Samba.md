# Samba 文件共享服务

```bash
sudo apt update
sudo apt install samba
```

编辑`/etc/samba/smb.conf`文件

```ini
[global]
        workgroup = SAMBA           #设定 Samba Server 所要加入的工作组或者域。
        security = user             #设置用户访问Samba Server的验证方式，一共有四种验证方式
        passdb backend = tdbsam
        printing = cups
        printcap name = cups
        load printers = yes
        cups options = raw
[myshare]
        comment = share myshare      #这个是共享文件的描述
        path = /path/to/share        #设置共享文件夹的路径
        public = no                  #设置是否允许匿名访问
        writable = yes
        browseable = yes
        create mask = 0755
        directory mask = 0755
```

创建Samba登录用户

```bash
useradd <username>
smbpasswd -a <username>

chmod -R 775 /path/to/share
```

访问共享文件

在Windows资源管理器中输入`\\address`即可访问对应的Samba服务器。

Linux访问Samba服务器

```bash
smbclient //192.168.0.102/myshare
```

