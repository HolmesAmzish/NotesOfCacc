### 在 Ubuntu Desktop 创建快捷方式的教程

在 Ubuntu 桌面（Ubuntu Desktop）上创建快捷方式，可以通过 `.desktop` 文件实现。这种方式适用于启动应用程序、脚本或特定目录。本文将介绍如何在 Ubuntu 上创建桌面快捷方式。

------

## 1. **了解 `.desktop` 文件**

`.desktop` 文件是一种用于定义应用程序启动方式的配置文件，存放于 `~/.local/share/applications/`（用户级）或 `/usr/share/applications/`（系统级）。它们用于创建桌面快捷方式或菜单项。

------

## 2. **创建快捷方式的步骤**

### **方法 1：手动创建 `.desktop` 文件**

#### **（1）打开终端**

按 `Ctrl + Alt + T` 组合键打开终端。

#### **（2）创建 `.desktop` 文件**

在 `~/Desktop` 目录下创建一个 `.desktop` 文件。例如，为 `Google Chrome` 创建快捷方式：

```bash
nano ~/Desktop/google-chrome.desktop
```

#### **（3）编辑 `.desktop` 文件**

在 `nano` 编辑器中，输入以下内容：

```ini
[Desktop Entry]
Version=1.0
Type=Application
Name=Google Chrome
Exec=/usr/bin/google-chrome-stable
Icon=/usr/share/icons/hicolor/128x128/apps/google-chrome.png
Terminal=false
Categories=Network;WebBrowser;
```

**参数说明：**

- `Version=1.0` —— 版本号
- `Type=Application` —— 类型（应用程序）
- `Name=Google Chrome` —— 应用显示的名称
- `Exec=/usr/bin/google-chrome-stable` —— 应用的执行路径
- `Icon=/usr/share/icons/hicolor/128x128/apps/google-chrome.png` —— 应用的图标路径
- `Terminal=false` —— 是否在终端中运行
- `Categories=Network;WebBrowser;` —— 归类到“网络”和“浏览器”类别

**保存文件**： 按 `Ctrl + X` → `Y` → `Enter` 退出并保存。

#### **（4）赋予执行权限**

运行以下命令，使快捷方式可执行：

```bash
chmod +x ~/Desktop/google-chrome.desktop
```

#### **（5）显示桌面图标**

如果 Ubuntu 桌面环境未启用桌面图标（如 GNOME 默认情况下），可能需要手动启用：

- 右键单击 `.desktop` 文件
- 选择 **“允许执行”**
- 双击即可运行

------

### **方法 2：从现有应用程序创建**

1. **查找 `.desktop` 文件** 许多已安装的应用程序的快捷方式存放在 `/usr/share/applications/`。
    运行以下命令找到目标应用：

   ```bash
   ls /usr/share/applications/
   ```

2. **复制到桌面**

   ```bash
   cp /usr/share/applications/google-chrome.desktop ~/Desktop/
   ```

3. **赋予权限**

   ```bash
   chmod +x ~/Desktop/google-chrome.desktop
   ```

------

## 3. **让快捷方式出现在应用菜单**

如果希望快捷方式出现在 Ubuntu 的“应用程序”菜单中，可以将 `.desktop` 文件复制到 `~/.local/share/applications/` 目录：

```bash
cp ~/Desktop/google-chrome.desktop ~/.local/share/applications/
```

然后在 **活动菜单** 或 **应用程序菜单** 中搜索 `Google Chrome`，即可看到新添加的快捷方式。

------

## 4. **删除快捷方式**

如果不再需要快捷方式，可以删除 `.desktop` 文件：

```bash
rm ~/Desktop/google-chrome.desktop
```

如果在 `~/.local/share/applications/` 目录中创建了快捷方式，可以运行：

```bash
rm ~/.local/share/applications/google-chrome.desktop
```

------

## 5. **额外功能**

### **（1）让脚本成为快捷方式**

如果你有一个 Bash 脚本 `my_script.sh`，并希望创建快捷方式：

```bash
nano ~/Desktop/my_script.desktop
```

输入：

```ini
[Desktop Entry]
Version=1.0
Type=Application
Name=My Script
Exec=/home/user/my_script.sh
Icon=utilities-terminal
Terminal=true
```

保存后赋予执行权限：

```bash
chmod +x ~/Desktop/my_script.desktop
```

### **（2）创建文件夹快捷方式**

```bash
nano ~/Desktop/my_folder.desktop
```

输入：

```ini
[Desktop Entry]
Type=Application
Name=My Folder
Exec=nautilus /home/user/Documents/
Icon=folder
Terminal=false
```

然后：

```bash
chmod +x ~/Desktop/my_folder.desktop
```

------

## 6. **结论**

通过 `.desktop` 文件，你可以轻松地在 Ubuntu 创建应用、脚本和文件夹的快捷方式，使操作更加便捷。