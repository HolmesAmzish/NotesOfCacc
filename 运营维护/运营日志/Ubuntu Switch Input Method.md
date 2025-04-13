设置切换输入法为例 `ctrl` + `shift` 。

```bash
gsettings set org.gnome.desktop.wm.keybindings switch-input-source "['<Primary>space']" 
```



以下是针对 **Ubuntu + Wayland** 环境下配置 **Fcitx5** 输入法的完整解决方案笔记，涵盖安装、配置、systemd 服务管理和常见问题排查：

---

# **Fcitx5 输入法配置指南 (Ubuntu + Wayland)**
## **1. 安装 Fcitx5**
```bash
sudo apt update
sudo apt install fcitx5 fcitx5-chinese-addons fcitx5-frontend-gtk3 fcitx5-frontend-qt5 fcitx5-configtool
```
> 📌 关键包说明：
> - `fcitx5`: 主程序  
> - `fcitx5-chinese-addons`: 中文输入支持（拼音/五笔）  
> - `fcitx5-frontend-gtk3/qt5`: GTK/Qt 程序输入支持  
> - `fcitx5-configtool`: 图形配置工具  

---

## **2. 配置环境变量**
编辑 `~/.pam_environment`（全局生效）或 `~/.profile`（用户级）：
```bash
# 适用于 Wayland/X11
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
export SDL_IM_MODULE=fcitx
export GLFW_IM_MODULE=ibus  # 部分游戏需要兼容性设置
```
**生效方式**：  
• 重新登录或重启系统  
• 临时测试：`source ~/.profile`

---

## **3. 配置 systemd 用户服务**
### **(1) 创建服务文件**
```bash
mkdir -p ~/.config/systemd/user/
cat > ~/.config/systemd/user/fcitx5.service <<EOF
[Unit]
Description=Fcitx5 Input Method
After=dbus.socket
Requires=dbus.socket

[Service]
Type=simple
ExecStart=/usr/bin/fcitx5 -d --replace
Restart=on-failure
RestartSec=3

[Install]
WantedBy=default.target
EOF
```
> 📌 关键参数说明：  
> - `Type=simple`: 标准服务类型（无需 D-Bus 总线名）  
> - `-d --replace`: 后台运行并替换现有实例  

### **(2) 启用并启动服务**
```bash
systemctl --user daemon-reload
systemctl --user enable --now fcitx5.service
systemctl --user status fcitx5.service  # 检查状态
```
> ✅ 预期输出：`active (running)`

---

## **4. Wayland 专属配置**
### **(1) 确保 Wayland 支持**
```bash
sudo apt install fcitx5-module-wayland
```
### **(2) 禁用 GNOME 默认输入法**
```bash
gsettings set org.gnome.desktop.input-sources sources "[('xkb', 'us')]"
```
### **(3) 检查 Wayland 环境变量**
```bash
echo $XDG_SESSION_TYPE  # 应输出 wayland
echo $WAYLAND_DISPLAY   # 应输出 wayland-0
```

---

## **5. 常见问题排查**
### **问题1：服务启动后立即退出**
• **原因**：Wayland 连接失败或 D-Bus 冲突  
• **解决**：  
  ```bash
  # 查看详细日志
  journalctl --user -u fcitx5.service -b
  # 手动调试启动
  fcitx5 -d --verbose=4
  ```

### **问题2：GTK/Qt 程序无法调出输入法**
• **原因**：环境变量未生效或前端未安装  
• **解决**：  
  ```bash
  # 确认前端已安装
  sudo apt install --reinstall fcitx5-frontend-gtk3 fcitx5-frontend-qt5
  # 检查变量是否泄漏（在终端中运行）
  env | grep IM_MODULE
  ```

### **问题3：系统重启后输入法失效**
• **原因**：systemd 用户服务未自动启动  
• **解决**：  
  ```bash
  # 启用 lingering 确保用户服务在登录前启动
  sudo loginctl enable-linger $USER
  ```

---

## **6. 完全卸载**
```bash
sudo apt purge fcitx5*
rm -rf ~/.config/fcitx5 ~/.local/share/fcitx5 ~/.config/systemd/user/fcitx5.service
systemctl --user daemon-reload
```

---

## **附：快速验证流程**
1. 安装后重启系统  
2. 运行 `fcitx5-configtool` 添加中文输入法（如拼音）  
3. 在终端输入 `fcitx5-diagnose` 检查所有配置项  
4. 测试输入法：  
   • GTK 程序：`gedit`  
   • Qt 程序：`pluma`（需安装）  

---

**完成！** 现在 Fcitx5 应该能在 Ubuntu Wayland 下稳定运行。如有其他问题，可通过 `journalctl --user -u fcitx5.service` 查看详细日志。
