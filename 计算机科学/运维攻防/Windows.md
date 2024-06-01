OpenSSH 是一款用于远程登录的连接工具，它使用 SSH 协议。 它会加密客户端与服务器之间的所有流量，从而遏止窃听、连接劫持和其他攻击。

OpenSSH 兼容的客户端可用于连接到 Windows Server 和 Windows 客户端设备。

> [!NOTE]
>
> 如果你是从 GitHub 存储库 ([PowerShell/Win32-OpenSSH](https://github.com/PowerShell/Win32-OpenSSH)) 下载的 OpenSSH 试用版，请按照该网页中列出的说明操作，而不是遵照本文列出的说明。 Win32-OpenSSH 存储库中的一些信息与预发行产品相关，相应产品在发行之前可能会进行重大修改。 Microsoft 不对此处提供的信息作任何明示或默示的担保。

## 先决条件

在开始之前，计算机必须满足以下要求：

- 至少运行 Windows Server 2019 或 Windows 10（内部版本 1809）的设备。
- PowerShell 5.1 或更高版本。
- 作为内置管理员组成员的帐户。



### 先决条件检查

若要验证环境，请打开提升的 PowerShell 会话并执行以下操作：

- 键入 *winver.exe* ，然后按 Enter 查看 Windows 设备的版本详细信息。

- 运行 `$PSVersionTable.PSVersion`。 验证主要版本至少为 5，次要版本至少为 1。 详细了解[如何在 Windows 上安装 PowerShell](https://learn.microsoft.com/zh-cn/powershell/scripting/install/installing-powershell-on-windows)。

- 运行下面的命令。 当你是内置 Administrator 组的成员时，输出将显示 `True`。

  PowerShell

  ```powershell
  (New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
  ```



## 安装适用于 Windows 的 OpenSSH

- [GUI](https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell#tabpanel_1_gui)
- [PowerShell](https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell#tabpanel_1_powershell)

若要使用 PowerShell 安装 OpenSSH，请先以管理员身份运行 PowerShell。 为了确保 OpenSSH 可用，请运行以下 cmdlet：

PowerShell

```powershell
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
```

如果两者均尚未安装，则此命令应返回以下输出：

Output

```Output
Name  : OpenSSH.Client~~~~0.0.1.0
State : NotPresent

Name  : OpenSSH.Server~~~~0.0.1.0
State : NotPresent
```

然后，根据需要安装服务器或客户端组件：

PowerShell

```powershell
# Install the OpenSSH Client
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

# Install the OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

这两个命令应会返回以下输出：

Output

```Output
Path          :
Online        : True
RestartNeeded : False
```

若要启动并配置 OpenSSH 服务器以供初始使用，请打开提升的 PowerShell 提示符（右键单击，以管理员身份运行），然后运行以下命令以启动 `sshd service`：

PowerShell

```powershell
# Start the sshd service
Start-Service sshd

# OPTIONAL but recommended:
Set-Service -Name sshd -StartupType 'Automatic'

# Confirm the Firewall rule is configured. It should be created automatically by setup. Run the following to verify
if (!(Get-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -ErrorAction SilentlyContinue | Select-Object Name, Enabled)) {
    Write-Output "Firewall Rule 'OpenSSH-Server-In-TCP' does not exist, creating it..."
    New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
} else {
    Write-Output "Firewall rule 'OpenSSH-Server-In-TCP' has been created and exists."
}
```



## 连接到 OpenSSH 服务器

安装后，可以从安装了 OpenSSH 客户端的 Windows 或 Windows Server 设备连接到 OpenSSH 服务器。 在 PowerShell 提示符下，运行以下命令。

PowerShell

```powershell
ssh domain\username@servername
```

连接后，会收到类似如以下输出的消息。

Output

```Output
The authenticity of host 'servername (10.00.00.001)' can't be established.
ECDSA key fingerprint is SHA256:(<a large string>).
Are you sure you want to continue connecting (yes/no)?
```

输入*“是”*会将该服务器添加到包含 Windows 客户端上的已知 SSH 主机的列表中。

此时，系统会提示输入密码。 作为安全预防措施，密码在键入的过程中不会显示。

连接后，你将看到 Windows 命令行界面提示符：

Output

```Output
domain\username@SERVERNAME C:\Users\username>
```



## 卸载适用于 Windows 的 OpenSSH

- [GUI](https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell#tabpanel_2_gui)
- [PowerShell](https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell#tabpanel_2_powershell)

若要使用 PowerShell 卸载 OpenSSH 组件，请使用以下命令：

PowerShell

```powershell
# Uninstall the OpenSSH Client
Remove-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

# Uninstall the OpenSSH Server
Remove-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

如果在卸载时服务正在使用中，稍后可能需要重启 Windows。



## 后续步骤

现在你已安装适用于 Windows 的 OpenSSH，下面一些文章可能对你的使用有帮助：

- 详细了解如何在 [OpenSSH 密钥管理](https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_keymanagement)中使用密钥对进行身份验证
- 详细了解[适用于 Windows 的 OpenSSH 服务器配置](https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_server_configuration)



```powershell
choco
```

- search
- install
- uninstall
- upgrade
- download