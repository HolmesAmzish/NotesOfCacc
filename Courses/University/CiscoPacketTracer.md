模式切换

```shell
enable
# 进入特权模式

configure terminal
# 进入全局配置模式

interface fastethernet 0/1
# 进入接口模式
```



修改交换机设置

```shell
hostname <name>
```



设置交换机接口

```shell
intface fastethernet 0/1
# int f0/1

shutdown
# 关闭一号接口

no shutdown
# 开启一号接口

int range f0/1-2
# 进入范围接口设置
```

