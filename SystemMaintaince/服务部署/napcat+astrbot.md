# Napcat

输入 xvfb-run -a qq --no-sandbox 命令启动。 
保持后台运行 请输入 screen -dmS napcat bash -c "xvfb-run -a qq --no-sandbox"  
后台快速登录 请输入 screen -dmS napcat bash -c "xvfb-run -a qq --no-sandbox -q QQ号码"  
Napcat安装位置 /opt/QQ/resources/app/app_launcher/napcat 
WEBUI_TOKEN 请自行查看/opt/QQ/resources/app/app_launcher/napcat/config/webui.json文件获取 
注意, 您可以随时使用 screen -r napcat 来进入后台进程并使用 ctrl + a + d 离开(离开不会关闭后台进程)。 
停止后台运行 请输入 screen -S napcat -X quit 



```ini
[Unit]
Description=Napcat QQ Client Headless Autostart
After=network.target

[Service]
Type=simple
User=your_username
Environment=DISPLAY=:99
ExecStart=/usr/bin/xvfb-run -a --server-num=99 --server-args="-screen 0 1024x768x24" /usr/bin/qq --no-sandbox -q 2519994926
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```



# AstrBot

```bash
python3 -m venv ./venv

source venv/bin/activate
python3 -m pip3 install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
python3 main.py
```



```ini
[Unit]
Description=AstrBot Startup Service
After=network.target

[Service]
Type=simple
User=cacc
WorkingDirectory=/home/cacc/AstrBot
ExecStart=/home/cacc/.local/bin/uv run main.py
Restart=always
RestartSec=5
Environment=PATH=/home/cacc/.local/bin:/usr/bin:/bin

[Install]
WantedBy=multi-user.target
```

