以下是使用 Zotero + WebDAV 的完整操作流程，包括 Apache2 设置 WebDAV、通过 frp 将 HTTP 转为 HTTPS，并使用 Certbot 生成证书的详细笔记。这份笔记将帮助你从头到尾配置一个可用于 Zotero（包括 iOS 版）的 WebDAV 服务。

---

# Zotero + WebDAV 配置完整笔记

## 目标
- 在本地服务器上通过 Apache2 配置 WebDAV 服务。
- 使用 frp 将本地 HTTP WebDAV 转换为 HTTPS，暴露到公网。
- 使用 Certbot 生成受信任的 SSL 证书，确保 Zotero iOS 支持。
- 配置 Zotero（桌面版和 iOS 版）以同步文件。

## 前提条件
- 一台 Linux 服务器（例如 Ubuntu），有公网 IP 或通过 frp 映射。
- 一个域名（例如 `yourdomain.com`），已解析到服务器 IP。
- Zotero 桌面版和 iOS 版已安装。

---

## 1. 配置 Apache2 WebDAV 服务

### 1.1 安装 Apache2
```bash
sudo apt update
sudo apt install apache2
```

### 1.2 启用 WebDAV 模块
```bash
sudo a2enmod dav
sudo a2enmod dav_fs
```

### 1.3 创建 WebDAV 目录
```bash
sudo mkdir -p /data/webdav
sudo chown www-data:www-data /data/webdav
sudo chmod 755 /data/webdav
```

### 1.4 创建 WebDAV 用户
使用 `htpasswd` 创建认证文件：
```bash
sudo htpasswd -c /etc/apache2/webdav.password zotero_user
```
- 输入密码（例如 `yourpassword`），记住用户名和密码，后续用于 Zotero 配置。

### 1.5 配置 Apache2 WebDAV
创建并编辑虚拟主机文件：
```bash
sudo nano /etc/apache2/sites-available/webdav.conf
```
写入以下内容：
```apache
<VirtualHost *:80>
    ServerAdmin admin@yourdomain.com
    DocumentRoot /data/webdav
    ServerName yourdomain.com

    <Directory /data/webdav>
        DAV On
        Options Indexes MultiViews
        IndexOptions Charset=UTF-8 FancyIndexing
        
        AuthType Basic
        AuthName "WebDAV Server"
        AuthUserFile /etc/apache2/webdav.password
        Require valid-user
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/webdav-error.log
    CustomLog ${APACHE_LOG_DIR}/webdav-access.log combined
</VirtualHost>
```

### 1.6 启用配置并重启 Apache
```bash
sudo a2ensite webdav.conf
sudo systemctl restart apache2
```
- 检查状态：
  ```bash
  sudo systemctl status apache2
  ```
- 测试本地访问：
  ```bash
  curl -u zotero_user:yourpassword http://127.0.0.1
  ```

---

## 2. 使用 Certbot 生成 SSL 证书

### 2.1 安装 Certbot
```bash
sudo apt install certbot
```

### 2.2 生成证书
- 停止 Apache（Certbot 需要占用 80 端口）：
  ```bash
  sudo systemctl stop apache2
  ```
- 生成证书：
  ```bash
  sudo certbot certonly --standalone -d yourdomain.com
  ```
- 证书文件生成在：
  - 证书：`/etc/letsencrypt/live/yourdomain.com/fullchain.pem`
  - 私钥：`/etc/letsencrypt/live/yourdomain.com/privkey.pem`

### 2.3 配置 Apache2 支持 HTTPS（可选）
如果想直接在 Apache 上启用 HTTPS：
```bash
sudo nano /etc/apache2/sites-available/webdav-ssl.conf
```
写入：
```apache
<VirtualHost *:443>
    ServerAdmin admin@yourdomain.com
    DocumentRoot /data/webdav
    ServerName yourdomain.com

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/yourdomain.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/yourdomain.com/privkey.pem

    <Directory /data/webdav>
        DAV On
        Options Indexes MultiViews
        IndexOptions Charset=UTF-8 FancyIndexing
        AuthType Basic
        AuthName "WebDAV Server"
        AuthUserFile /etc/apache2/webdav.password
        Require valid-user
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/webdav-error.log
    CustomLog ${APACHE_LOG_DIR}/webdav-access.log combined
</VirtualHost>
```
启用并重启：
```bash
sudo a2enmod ssl
sudo a2ensite webdav-ssl.conf
sudo systemctl restart apache2
```

---

## 3. 配置 frp 将 HTTP 转为 HTTPS

### 3.1 下载并安装 frp
- 下载最新版本（例如 0.61.1）：
  ```bash
  wget https://github.com/fatedier/frp/releases/download/v0.61.1/frp_0.61.1_linux_amd64.tar.gz
  tar -xzf frp_0.61.1_linux_amd64.tar.gz
  cd frp_0.61.1_linux_amd64
  ```

### 3.2 配置 frp 服务端（frps）
- 编辑 `frps.toml`：
  ```bash
  nano frps.toml
  ```
  内容：
  ```toml
  bindPort = 7000
  vhostHTTPSPort = 443
  ```
- 启动 frps（假设在公网服务器上）：
  ```bash
  ./frps -c frps.toml
  ```

### 3.3 配置 frp 客户端（frpc）
- 编辑 `webdav.toml`：
  ```bash
  nano webdav.toml
  ```
  内容：
  ```toml
  serverAddr = "x.x.x.x"  # 替换为 frps 的公网 IP
  serverPort = 7000
  
  [[proxies]]
  name = "talos-webdav"
  type = "https"
  customDomains = ["yourdomain.com"]
  
  [proxies.plugin]
  type = "https2http"
  localAddr = "127.0.0.1:80"
  crtPath = "/etc/letsencrypt/live/yourdomain.com/fullchain.pem"
  keyPath = "/etc/letsencrypt/live/yourdomain.com/privkey.pem"
  ```
- 启动 frpc：
  ```bash
  ./frpc -c webdav.toml
  ```

### 3.4 设置 frp 开机自启（可选）
- 创建 systemd 服务：
  ```bash
  sudo nano /etc/systemd/system/frp-webdav.service
  ```
  内容：
  ```ini
  [Unit]
  Description=FRP WebDAV Client
  After=network.target
  
  [Service]
  ExecStart=/opt/frp_0.61.1_linux_amd64/frpc -c /opt/frp_0.61.1_linux_amd64/webdav.toml
  Restart=always
  
  [Install]
  WantedBy=multi-user.target
  ```
- 启用服务：
  ```bash
  sudo systemctl daemon-reload
  sudo systemctl enable frp-webdav
  sudo systemctl start frp-webdav
  ```

### 3.5 验证 frp 配置
- 检查日志：
  ```bash
  ./frpc -c webdav.toml --log-level=debug
  ```
- 浏览器访问 `https://yourdomain.com`，输入 `zotero_user:yourpassword`，应看到 WebDAV 目录。

---

## 4. 配置 Zotero 使用 WebDAV

### 4.1 Zotero 桌面版
1. 打开 Zotero > 编辑 > 首选项 > 同步。
2. 在“文件同步”部分：
   - 选择“WebDAV”。
   - 地址：`https://yourdomain.com`
   - 用户名：`zotero_user`
   - 密码：`yourpassword`
3. 点击“验证服务器”，应显示成功。
4. 点击“确定”，开始同步。

### 4.2 Zotero iOS 版
1. 打开 Zotero iOS > 设置 > 同步。
2. 在“文件同步”部分：
   - WebDAV 地址：`https://yourdomain.com`
   - 用户名：`zotero_user`
   - 密码：`yourpassword`
3. 点击“验证服务器”，确认成功。
4. 返回主界面，触发同步。

---

## 5. 故障排查

### 5.1 Apache2 问题
- 检查状态：
  ```bash
  sudo systemctl status apache2
  sudo journalctl -xeu apache2.service
  ```
- 测试配置：
  ```bash
  sudo apache2ctl configtest
  ```

### 5.2 frp 问题
- 查看日志：
  ```bash
  ./frps -c frps.toml --log-level=debug
  ./frpc -c webdav.toml --log-level=debug
  ```
- 检查端口：
  ```bash
  sudo netstat -tuln | grep "7000\|443"
  ```

### 5.3 证书问题
- 验证证书：
  ```bash
  openssl x509 -in /etc/letsencrypt/live/yourdomain.com/fullchain.pem -text -noout
  ```
- 测试 HTTPS：
  ```bash
  curl -v https://yourdomain.com
  ```

### 5.4 Zotero 连接失败
- 确保地址不带斜杠（如 `https://yourdomain.com`，而不是 `https://yourdomain.com/`）。
- 检查用户名和密码是否正确。

---

## 6. 注意事项
- **域名解析**：确保 `yourdomain.com` 已指向服务器 IP。
- **防火墙**：开放 80、443、7000 端口：
  ```bash
  sudo ufw allow 80
  sudo ufw allow 443
  sudo ufw allow 7000
  ```
- **证书续期**：Let's Encrypt 证书有效期 90 天，设置自动续期：
  ```bash
  sudo certbot renew --dry-run
  ```

---

## 7. 最终效果
- 本地 Apache WebDAV 服务通过 `http://127.0.0.1:80` 运行。
- frp 将其转发为 `https://yourdomain.com`，使用受信任证书。
- Zotero 桌面版和 iOS 版通过 HTTPS WebDAV 同步文献附件。

这份笔记涵盖了从零开始的完整配置流程，可作为参考或故障排查依据。如果有任何问题，可以随时补充日志或具体步骤，我会帮你调整！