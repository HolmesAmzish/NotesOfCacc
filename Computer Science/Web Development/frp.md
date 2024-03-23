# frps

```toml
bindPort = 7000

webServer.addr = "0.0.0.0"
webServer.port = 7500
webServer.user = "admin"
webServer.password = "admin"
```



# frpc

## 一般配置

```toml
serverAddr = "x.x.x.x"
serverPort = 7000

[[proxies]]
name = "ssh"
type = "tcp"
localIP = "127.0.0.1"
localPort = 22
remotePort = 6000
```



## 配置拆分

```toml
serverAddr = "frp.arorms.cn"
serverPort = 7000
includes = ["./confd/*.toml"]
```

```toml
# ./confd/test.toml
[[proxies]]
name = "ssh"
type = "tcp"
localIP = "127.0.0.1"
localPort = 22
remotePort = 6000
```

