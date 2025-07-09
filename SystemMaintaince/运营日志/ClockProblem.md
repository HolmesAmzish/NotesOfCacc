在双系统环境下，Windows 和 Ubuntu 对硬件时间的处理方式不同，可能导致时间显示不一致的问题。具体而言，Windows 将硬件时间视为本地时间，而 Ubuntu 默认将硬件时间视为协调世界时（UTC）。这种差异会导致在切换操作系统后，时间显示出现偏差。

**解决方法：**

为了使两个系统的时间保持一致，可以通过以下两种方法之一进行调整：

1. **在 Ubuntu 中将硬件时间设置为本地时间：**

   这使得 Ubuntu 与 Windows 采用相同的时间处理方式。

   - 打开终端，输入以下命令：

     ```bash
     timedatectl set-local-rtc 1 --adjust-system-clock
     ```

   - 此命令将 Ubuntu 的硬件时间设置为本地时间，并自动调整系统时钟。

   完成后，重启 Ubuntu 系统。

   

2. **在 Windows 中将硬件时间设置为 UTC：**

   这使得 Windows 与 Ubuntu 采用相同的时间处理方式。

   - 按下 `Win + R` 键，输入 `regedit`，打开注册表编辑器。

   - 导航到以下路径：

     ```bash
     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation
     ```

   - 在右侧窗口中，右键选择“新建” > “DWORD（32位）值”，将其命名为 `RealTimeIsUniversal`。

   - 双击新建的 `RealTimeIsUniversal`，将数值数据设置为 `1`，然后点击“确定”。

   - 关闭注册表编辑器，重启 Windows 系统。

   

请注意，以上两种方法任选其一即可，无需同时进行。调整后，Windows 和 Ubuntu 的时间显示应保持一致。