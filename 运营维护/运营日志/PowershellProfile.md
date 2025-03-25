列出所有命令行自启动设置文件

```powershell
$PROFILE | Get-Member -MemberType NoteProperty
```

输出示例：

```
AllUsersAllHosts       : C:\Program Files\PowerShell\7\profile.ps1
AllUsersCurrentHost    : C:\Program Files\PowerShell\7\Microsoft.PowerShell_profile.ps1
CurrentUserAllHosts    : C:\Users\YourName\Documents\PowerShell\profile.ps1
CurrentUserCurrentHost : C:\Users\YourName\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
```

编辑

```powershell
notepad C:\Users\Holme\Documents\WindowsPowerShell\profile.ps1
```

