# Zerotier

Zerotier是一个内网穿透软件，他会创建一个虚拟局域网，将安装客户端的主机连接起来，形成一个虚拟局域网，实现相互间通信而不需要暴露在公网上。

主要工作原理通过VPN隧道，实现主机间P2P通信。除此之外，如果机器间创建隧道失败，会通过转发服务器进行流量转发。

## 下载Zerotier

官网下载地址：https://www.zerotier.com/download/

Linux服务器可以通过官方指令直接下载

```bash
curl -s https://install.zerotier.com | sudo bash
```

下载完成后，Windows和Linux一般都会设置成开机自启动，并且Windows会带一个UI。

## 加入虚拟组网

通过在Zerotier管理页面的虚拟网络ID加入，客户端可以通过UI添加，也可以通过命令行。

```bash
sudo zerotier-cli join <network_id>
```

## 搭建Moon服务器

如果无法直接打通隧道，那么会通过中转服务器将流量进行转发。然而Zerotier的服务器位于国外，并且流量需要加密，会导致延迟非常高。如果无法进行P2P方式连接，那么就需要自己在国内搭建一个Moon服务器用于转发流量。

Moon服务器需要能暴露在公网中，而且对机器的算力要求不高。最优的方法就是组一个2核512MB内存的云服务器，运营商可以自己选择。

### 服务器设置

首先将要作为Moon服务器的主机添加进虚拟网络。

```bash
sudo zerotier-cli join <network_id>
```

加入成功后，需要进入Zerotier的配置文件目录并生成moon.json文件，这是本机的信息，等会用于生成对应的签名。

```bash
cd /var/lib/zerotier-one
sudo zerotier-idtool initmoon identity.public >> moon.json
```

然后编辑moon.json文件，编辑信息，其他不用动，找到`stableEndpoints`这里，添加`"ip_address/9993"`，如果需要添加一个ipv6地址，可以用逗号分隔。

编辑完后生成.moon 签名文件

```bash
zerotier-idtool genmoon moon.json
```

这样会生成一个六个前导0加上本主机在zerotier上的id的moon签名文件，将本文件转移到同目录下的moons.d文件夹并重启zerotier-one生效。

```bash
cp 000000xxxxxxxxx.moon moons.d/
sudo systemctl restart zerotier-one
```

> [!NOTE]
> 
> 特别注意，编辑moon.json时地址必须是IP地址而不是域名。云服务器一般都有安全策略，需要放行服务器端口9993 TCP和UDP的连接。

### 客户端设置

客户端需要手动选择认定本服务器为Moon服务器，首先要知道Moon服务器的ID，这个可以在Zerotier管理页面上看，刚刚编辑的moon.json中也是他的ID。如果你是Windows系统，那么需要以管理员身份启动终端。

```bash
sudo zerotier-cli orbit <id> <id>
sudo systemctl restart zerotier-one
```

随后提示OK，则表明指定成功。可以通过指令查看是否添加完成。随后重启。Windows需要在服务中重启Zerotier服务。

```bash
sudo zerotier-cli listpeers
```

这个指令会显示所有节点，其中PLANET字样的为官方节点，LEAF为普通节点，而MOON为你刚刚设置的Moon服务器。

除了直接通过命令，还可以将服务器生成的签名文件下载到本地，移动到客户端的配置文件夹并重启服务。文件位置如下：

```
Windows: C:\ProgramData\ZeroTier\One
Linux: /var/lib/zerotier-one
FreeBSD/OpenBSD: /var/db/zerotier-one
```
