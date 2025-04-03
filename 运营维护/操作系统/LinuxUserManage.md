## 提权

以管理员方式运行命令

```bash
sudo <command>
```

进入管理员 root 身份

```bash
su
```





## Debian 系统将普通用户添加到 sudoers

**编辑 `/etc/sudoers/` 名单**

```bash
visudo # equals "vim /etc/sudoers"
```

在文件中添加以下行

```ini
username ALL=(ALL:ALL) ALL
```

或者添加**子配置文件**

```bash
echo "cacc ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/cacc
```

