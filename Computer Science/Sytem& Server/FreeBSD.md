# 系统管理

## 服务

编写启动脚本, 一般位于/usr/local/etc/rc.d/或者/etc/rc.d/, 后者一般是系统设定脚本. 脚本为无扩展名的文件, 格式为:

```ini
#!/bin/sh

# PROVIDE: frpc_ssh
# REQUIRE: NETWORKING SERVERS
# KEYWORD: shutdown

. /etc/rc.subr

name="frpc_ssh"
rcvar="frpc_ssh_enable"
start_cmd="frpc_ssh_start"
stop_cmd="frpc_ssh_stop"

frpc_ssh_start() {
    nohup /opt/frp/frpc -c /opt/frp/ssh.toml &
}

frpc_ssh_stop() {
    pkill -f "frpc -c ssh.toml"
}

load_rc_config $name
run_rc_command "1"
```

```ini
#!/bin/sh

# PROVIDE: star_frpc_ssh
# REQUIRE: NETWORKING SERVERS
# KEYWORD: shutdown

. /etc/rc.subr

name="star_frpc_ssh"
rcvar="star_frpc_ssh_enable"
start_cmd="star_frpc_ssh_start"
stop_cmd="star_frpc_ssh_stop"

star_frpc_ssh_start() {
    nohup /opt/frpc_starry/frpc -f c3867d3c81ee8403eeed309304ae192a:101568 >/dev/null 2>&1 &
}

star_frpc_ssh_stop() {
    pkill -f "frpc -f c3867d3c81ee8403eeed309304ae192a:101568"
}

load_rc_config $name
run_rc_command "$1"
```

之后可用`service`命令进行控制, 而服务名即为文件名

```bash
service frpc_ssh start
```

如果要设置开机子启动,前往/etc/rc.conf修改一行frpc_ssh_enable="YES",或者使用指令修改

```bash
service frpc_ssh enable
```
