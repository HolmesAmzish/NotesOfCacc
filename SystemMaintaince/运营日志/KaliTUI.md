---
title: Kali 图形化或命令行界面
date: 2025-03-24
author: Holmes Amzish
---

查看当前开机默认进入界面

```bash
systemctl get-default
```

修改开机默认进入界面

```bash
systemctl set-default graphical.target

systemctl set-default multi-user.target
```



