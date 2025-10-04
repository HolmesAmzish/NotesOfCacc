最近这几天服务器总是掉线，要查一下服务器的问题。可以首先查看一下计算机硬件，这是一台某鱼上拼凑的服务器：

```bash
sudo lshw -short
```

```
H/W path           Device          Class          Description
=============================================================
                                   system         NF5270M3 (To be filled by O.E.M.)
/0                                 bus            NF5270M3
/0/0                               memory         64KiB BIOS
/0/4                               processor      Intel(R) Xeon(R) CPU E5-2630 v2 @ 2.60GHz
/0/4/5                             memory         384KiB L1 cache
/0/4/6                             memory         1536KiB L2 cache
/0/4/7                             memory         15MiB L3 cache
/0/6                               processor      Intel(R) Xeon(R) CPU E5-2630 v2 @ 2.60GHz
/0/6/9                             memory         384KiB L1 cache
/0/6/a                             memory         1536KiB L2 cache
/0/6/b                             memory         15MiB L3 cache
/0/2c                              memory         24GiB System Memory
/0/2c/0                            memory         8GiB DIMM DDR3 1066 MHz (0.9 ns)
/0/2c/1                            memory         DIMM Synchronous [empty]
/0/2c/2                            memory         DIMM Synchronous [empty]
/0/2c/3                            memory         DIMM Synchronous [empty]
/0/2c/4                            memory         DIMM Synchronous [empty]
/0/2c/5                            memory         DIMM Synchronous [empty]
/0/2c/6                            memory         8GiB DIMM DDR3 1066 MHz (0.9 ns)
/0/2c/7                            memory         DIMM Synchronous [empty]
/0/2c/8                            memory         DIMM Synchronous [empty]
/0/2c/9                            memory         DIMM Synchronous [empty]
/0/2c/a                            memory         DIMM Synchronous [empty]
/0/2c/b                            memory         DIMM Synchronous [empty]
/0/2c/c                            memory         8GiB DIMM DDR3 1066 MHz (0.9 ns)
/0/2c/d                            memory         DIMM Synchronous [empty]
/0/2c/e                            memory         DIMM Synchronous [empty]
/0/2c/f                            memory         8GiB DIMM DDR3 1066 MHz (0.9 ns)
/0/2c/10                           memory         DIMM Synchronous [empty]
/0/2c/11                           memory         DIMM Synchronous [empty]
/0/2c/12                           memory         DIMM Synchronous [empty]
/0/2c/13                           memory         DIMM Synchronous [empty]
/0/100/3/0         /dev/nvme0      storage        LITEON CA3-8D128-HP
/0/100/3/0/0       hwmon0          disk           NVMe disk
/0/100/3/0/2       /dev/ng0n1      disk           NVMe disk
/0/100/3/0/1       /dev/nvme0n1    disk           128GB NVMe disk
/0/100/3/0/1/1                     volume         1074MiB Windows FAT volume
/0/100/3/0/1/2     /dev/nvme0n1p2  volume         2GiB EXT4 volume
/0/100/3/0/1/3     /dev/nvme0n1p3  volume         116GiB EFI partition
/0/100/1f.2/0      /dev/sda        disk           500GB WDC WD5000AAKX-0
/0/100/1f.2/0/1    /dev/sda1       volume         465GiB EXT4 volume
/0/100/1f.2/1      /dev/sdb        disk           500GB WDC WD5000AAKX-2
/0/100/1f.2/1/1    /dev/sdb1       volume         465GiB EXT4 volume

```

网络掉线后插上 HDMI 显示屏查看屏幕显示状态，发现 Memory 相关字样，推测可能和内存条错误有关。

重启后查看系统日志：

```bash
tail -200 /var/log/syslog
```

```
2025-04-04T18:23:54.720029+08:00 talos kernel: Memory failure: 0x46fab5: unhandlable page.
2025-04-04T18:23:55.230128+08:00 talos kernel: {3}[Hardware Error]: Hardware error from APEI Generic Hardware Error Source: 1
2025-04-04T18:23:55.230140+08:00 talos kernel: {3}[Hardware Error]: It has been corrected by h/w and requires no further action
2025-04-04T18:23:55.230141+08:00 talos kernel: {3}[Hardware Error]: event severity: corrected
2025-04-04T18:23:55.230143+08:00 talos kernel: {3}[Hardware Error]: Error 0, type: corrected
2025-04-04T18:23:55.230144+08:00 talos kernel: {3}[Hardware Error]: fru_text: CorrectedErr
2025-04-04T18:23:55.230145+08:00 talos kernel: {3}[Hardware Error]: section_type: memory error
2025-04-04T18:23:55.230146+08:00 talos kernel: {3}[Hardware Error]: node:0 device:0 
2025-04-04T18:23:55.230147+08:00 talos kernel: {3}[Hardware Error]: error_type: 2, single-bit ECC
2025-04-04T18:24:01.695052+08:00 talos kernel: RAS: Soft-offlining pfn: 0x104e5c
2025-04-04T18:24:01.695076+08:00 talos kernel: EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
2025-04-04T18:24:01.695080+08:00 talos kernel: EDAC sbridge MC0: CPU 0: Machine Check Event: 0 Bank 7: cc00050000010092
2025-04-04T18:24:01.695082+08:00 talos kernel: EDAC sbridge MC0: TSC 0 
2025-04-04T18:24:01.695084+08:00 talos kernel: EDAC sbridge MC0: ADDR 104e5c8c0 
2025-04-04T18:24:01.695086+08:00 talos kernel: EDAC sbridge MC0: MISC 40584e86 
2025-04-04T18:24:01.695088+08:00 talos kernel: EDAC sbridge MC0: PROCESSOR 0:306e4 TIME 1743762241 SOCKET 0 APIC 0
2025-04-04T18:24:01.695090+08:00 talos kernel: EDAC MC0: 20 CE memory read error on CPU_SrcID#0_Ha#0_Chan#2_DIMM#0 (channel:2 slot:0 page:0x104e5c offset:0x8c0 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:4 rank:1 )
2025-04-04T18:24:01.695094+08:00 talos kernel: Memory failure: 0x104e5c: unhandlable page.
```

从系统日志中可以看出，系统正在经历严重的内存错误（Memory Errors），主要涉及硬件层面的问题。



检查详细错误日志：

```bash
sudo dmesg | grep -i error
```

```
[19108.267949] {2}[Hardware Error]: Hardware error from APEI Generic Hardware Error Source: 1
[19108.267972] {2}[Hardware Error]: It has been corrected by h/w and requires no further action
[19108.267976] {2}[Hardware Error]: event severity: corrected
[19108.267985] {2}[Hardware Error]:  Error 0, type: corrected
[19108.267992] {2}[Hardware Error]:  fru_text: CorrectedErr
[19108.267997] {2}[Hardware Error]:   section_type: memory error
[19108.268003] {2}[Hardware Error]:   node:0 device:0 
[19108.268005] {2}[Hardware Error]:   error_type: 2, single-bit ECC
[19114.873932] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19114.874122] EDAC MC0: 16385 CE memory read error on CPU_SrcID#0_Ha#0_Chan#2_DIMM#0 (channel:2 slot:0 page:0x46f934 offset:0xbc0 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:4 rank:1 )
[19118.239275] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19118.239533] EDAC MC0: 25284 CE memory read error on CPU_SrcID#0_Ha#0_Chan#2_DIMM#0 (channel:2 slot:0 page:0x46fb35 offset:0x5c0 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:4 rank:1 )
[19128.825566] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19128.825743] EDAC MC0: 16708 CE memory read error on CPU_SrcID#0_Ha#0_Chan#2_DIMM#0 (channel:2 slot:0 page:0x46fab5 offset:0x5c0 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:4 rank:1 )
[19133.700096] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19133.700127] EDAC MC0: 32750 CE memory read error on CPU_SrcID#0_Ha#0_Chan#2_DIMM#0 (channel:2 slot:0 page:0x46f834 offset:0xbc0 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:4 rank:1 )
[19135.870233] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19135.870309] EDAC MC0: 16687 CE memory read error on CPU_SrcID#0_Ha#0_Chan#2_DIMM#0 (channel:2 slot:0 page:0x46fa34 offset:0xbc0 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:4 rank:1 )
[19138.224432] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19138.224502] EDAC MC0: 15745 CE memory read error on CPU_SrcID#0_Ha#0_Chan#0_DIMM#0 (channel:0 slot:0 page:0x46fcb4 offset:0xd80 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:1 rank:1 )
[19140.213293] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19140.213328] EDAC MC0: 15575 CE memory read error on CPU_SrcID#0_Ha#0_Chan#2_DIMM#0 (channel:2 slot:0 page:0x10aac5 offset:0x1c0 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:4 rank:1 )
[19141.210137] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19141.210164] EDAC MC0: 19211 CE memory read error on CPU_SrcID#0_Ha#0_Chan#2_DIMM#0 (channel:2 slot:0 page:0x46fab4 offset:0xbc0 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:4 rank:1 )
[19141.906759] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19141.906780] EDAC MC0: 16437 CE memory read error on CPU_SrcID#0_Ha#0_Chan#2_DIMM#0 (channel:2 slot:0 page:0x46f9b4 offset:0xbc0 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:4 rank:1 )
[19143.127824] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19143.127876] EDAC MC0: 24609 CE memory read error on CPU_SrcID#0_Ha#0_Chan#0_DIMM#0 (channel:0 slot:0 page:0x46f835 offset:0x680 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:1 rank:1 )
[19145.175716] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19145.175754] EDAC MC0: 5555 CE memory read error on CPU_SrcID#0_Ha#0_Chan#0_DIMM#0 (channel:0 slot:0 page:0x7f3ec offset:0x280 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:1 rank:1 )
[19148.183616] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19148.183654] EDAC MC0: 4858 CE memory read error on CPU_SrcID#0_Ha#0_Chan#0_DIMM#0 (channel:0 slot:0 page:0x1021ad offset:0x180 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:1 rank:1 )
[19149.143580] mce: [Hardware Error]: Machine check events logged
[19149.143583] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19149.143619] EDAC MC0: 4223 CE memory read error on CPU_SrcID#0_Ha#0_Chan#2_DIMM#0 (channel:2 slot:0 page:0x7f3ee offset:0xec0 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:4 rank:1 )
[19149.143629] mce: [Hardware Error]: Machine check events logged
[19151.167012] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19151.167036] EDAC MC0: 4119 CE memory read error on CPU_SrcID#0_Ha#0_Chan#0_DIMM#0 (channel:0 slot:0 page:0x7f3ec offset:0x280 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:1 rank:1 )
[19152.151462] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19152.151502] EDAC MC0: 3976 CE memory read error on CPU_SrcID#0_Ha#0_Chan#0_DIMM#0 (channel:0 slot:0 page:0x46f835 offset:0x680 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:1 rank:1 )
[19153.175444] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19153.175485] EDAC MC0: 24245 CE memory read error on CPU_SrcID#0_Ha#0_Chan#2_DIMM#0 (channel:2 slot:0 page:0x46fc34 offset:0x9c0 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:4 rank:1 )
[19169.174851] EDAC sbridge MC0: HANDLING MCE MEMORY ERROR
[19169.174898] EDAC MC0: 48 CE memory read error on CPU_SrcID#0_Ha#0_Chan#2_DIMM#0 (channel:2 slot:0 page:0x46fab5 offset:0x3c0 grain:32 syndrome:0x0 -  OVERFLOW area:DRAM err_code:0001:0092 socket:0 ha:0 channel_mask:4 rank:1 )
```

从 `dmesg` 输出的硬件错误日志来看，系统正在经历**严重的ECC内存错误**，主要集中在 **Channel 2, DIMM 0** 和 **Channel 0, DIMM 0**。



内存插槽与 CPU 信息

```bash
sudo dmidecode -t memory | grep -A10 "Memory Device$" | egrep "Locator|Bank Locator|Size"
```

```

	Size: 8 GB
	Locator: Node0_Dimm0
	Bank Locator: Node0_Bank0
	Size: No Module Installed
	Locator: Node0_Dimm1
	Bank Locator: Node0_Bank0
	Size: No Module Installed
	Locator: Node0_Dimm2
	Bank Locator: Node0_Bank0
	Size: No Module Installed
	Locator: Node0_Dimm3
	Bank Locator: Node0_Bank0
	Size: No Module Installed
	Locator: Node0_Dimm4
	Bank Locator: Node0_Bank0
	Size: No Module Installed
	Locator: Node0_Dimm5
	Bank Locator: Node0_Bank0
	Size: 8 GB
	Locator: Node0_Dimm6
	Bank Locator: Node0_Bank0
	Size: No Module Installed
	Locator: Node0_Dimm7
	Bank Locator: Node0_Bank0
	Size: No Module Installed
	Locator: Node0_Dimm8
	Bank Locator: Node0_Bank0
	Size: No Module Installed
	Locator: Node0_Dimm9
	Bank Locator: Node0_Bank0
	Size: No Module Installed
	Locator: Node0_Dimm10
	Bank Locator: Node0_Bank0
	Size: No Module Installed
	Locator: Node0_Dimm11
	Bank Locator: Node0_Bank0
	Size: 8 GB
	Locator: Node1_Dimm0
	Bank Locator: Node1_Bank0
	Size: No Module Installed
	Locator: Node1_Dimm1
	Bank Locator: Node1_Bank0
	Size: No Module Installed
	Locator: Node1_Dimm2
	Bank Locator: Node1_Bank0
	Size: No Module Installed
	Locator: Node1_Dimm3
	Bank Locator: Node1_Bank0
	Size: 8 GB
	Locator: Node1_Dimm4
	Bank Locator: Node1_Bank0
	Size: No Module Installed
	Locator: Node1_Dimm5
	Bank Locator: Node1_Bank0
	Size: No Module Installed
	Locator: Node1_Dimm6
	Bank Locator: Node1_Bank0
	Size: No Module Installed
	Locator: Node1_Dimm7
	Bank Locator: Node1_Bank0
```

从上可以看出应该是 CPU0 的第一个插槽。直接将本插槽的内存条移出恢复正常。