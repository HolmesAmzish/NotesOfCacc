Official site: https://redis.io/

**Install**

```bash
sudo apt install redis-server
```

**Usage**

```bash
redis-cli  # Enter redis command line interface
redis-cli <command>  # Run command of redis
```



Redis 将数据存储在内存实现快速IO操作，比一般数据库通过硬盘持久化存储效率更高。同时基于内存存储需要设置阈值以管理内存大小，通过淘汰机制和持久化机制来管理数据。

Redis 存储机制类似于一般程序将变量存储在内存中，速度快。同时 Redis 作为一个独立的统一的服务器框架提供了更多接口与组织模式选择。



Redis 应用场景

1. Token 令牌的生成
2. 短信验证码存储
3. 查询数据缓存（减轻数据库访问压力