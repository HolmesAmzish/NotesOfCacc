# 网络

## netstat 监听端口占用

```powershell
netstat
Get-NetTCPConnection
```

```powershell
netstat -a
# 显示windows正在监听的所有活动链接
```

- `-o`显示每个进程的PID
- `-n`以数值形式显示IP的地址和端口

```powershell
netstat -ano | findstr /i listening
```

# 文件

## 子项目

```powershell
Get-ChildItem . -File | Where-Object { $_.Extension -eq ".html" }
tree /f | Select-String "html"
```

