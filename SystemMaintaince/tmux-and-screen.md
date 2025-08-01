---
title: Tmux & Screen, multiple sessions in Linux
date: 2025-07-20
author: Cacciatore
---

| 功能类别         | Tmux 命令/快捷键                 | Screen 命令/快捷键             | 说明                  |
| ---------------- | -------------------------------- | ------------------------------ | --------------------- |
| **启动会话**     | `tmux` 或 `tmux new -s <name>`   | `screen` 或 `screen -S <name>` | 创建新会话            |
| **列出现有会话** | `tmux ls`                        | `screen -ls`                   | 查看当前所有会话      |
| **附加会话**     | `tmux attach -t <name>`          | `screen -r <name>`             | 恢复/附加已存在的会话 |
| **分离会话**     | `Ctrl+b d`                       | `Ctrl+a d`                     | 分离会话，回到主终端  |
| **重命名会话**   | `tmux rename-session -t old new` | `Ctrl+a A`                     | 更改会话名            |
| **结束会话**     | 输入 `exit` 或 `Ctrl+d`          | 输入 `exit` 或 `Ctrl+d`        | 关闭当前会话窗口      |
| **杀死会话**     | `tmux kill-session -t <name>`    | `screen -X -S <name> quit`     | 强制终止会话          |

| 操作           | Tmux                                                         | Screen                             | 说明           |
| -------------- | ------------------------------------------------------------ | ---------------------------------- | -------------- |
| **新建窗口**   | `Ctrl+b c`                                                   | `Ctrl+a c`                         | 创建新窗口     |
| **切换窗口**   | `Ctrl+b n`（下一个）`Ctrl+b p`（上一个）`Ctrl+b <0-9>`（指定窗口） | `Ctrl+a n``Ctrl+a p``Ctrl+a <0-9>` | 在窗口间切换   |
| **重命名窗口** | `Ctrl+b ,`                                                   | `Ctrl+a A`                         | 修改当前窗口名 |
| **关闭窗口**   | 输入 `exit` 或 `Ctrl+d`                                      | 同左                               | 关闭当前窗口   |

| 操作         | Tmux 快捷键                         | 说明                           |
| ------------ | ----------------------------------- | ------------------------------ |
| **垂直分屏** | `Ctrl+b %`                          | 左右分屏                       |
| **水平分屏** | `Ctrl+b "`                          | 上下分屏                       |
| **切换面板** | `Ctrl+b o`                          | 在面板之间切换                 |
| **调整大小** | `Ctrl+b + ←/→/↑/↓`                  | 使用方向键调整面板大小         |
| **关闭面板** | `exit` 或 `Ctrl+d`                  | 关闭当前面板                   |
| **同步输入** | `Ctrl+b :setw synchronize-panes on` | 所有面板同步输入（`off` 关闭） |

| 功能               | Tmux                                | Screen                  | 说明                   |
| ------------------ | ----------------------------------- | ----------------------- | ---------------------- |
| **复制模式**       | `Ctrl+b [` 然后移动光标，按回车复制 | `Ctrl+a [` 进入复制模式 | 用于查看历史和复制文本 |
| **粘贴**           | `Ctrl+b ]`                          | `Ctrl+a ]`              | 粘贴复制的内容         |
| **查看快捷键帮助** | `Ctrl+b ?`                          | `Ctrl+a ?`              | 显示所有快捷键         |

| 工具       | 配置文件       | 说明                 |
| ---------- | -------------- | -------------------- |
| **tmux**   | `~/.tmux.conf` | 启动时加载的配置文件 |
| **screen** | `~/.screenrc`  | 启动时加载的配置文件 |