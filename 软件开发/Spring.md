pom.xml 配置

```xml
<dependencies>
    <!-- Spring Core -->
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-core</artifactId>
        <version>5.3.30</version>
    </dependency>

    <!-- Spring Beans -->
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-beans</artifactId>
        <version>5.3.30</version>
    </dependency>

    <!-- Spring Context -->
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.3.30</version>
    </dependency>
</dependencies>
```



## spring-context

### @Schedule

使用前需要先启用。修饰主程序。

```
@EnableScheduling
```



`@Scheduled`注解中的`cron`表达式采用的是标准的UNIX cron格式，由六个部分组成，分别用于定义任务的触发时间。格式如下：

```
复制代码
秒 分 时 日 月 周
```

每个部分的含义如下：

1. **秒**（0 - 59）
2. **分**（0 - 59）
3. **小时**（0 - 23）
4. **日期**（1 - 31）
5. **月份**（1 - 12）
6. **星期几**（0 - 7，0和7都表示周日）

### 特殊符号

- **`\*`**：代表任意值。例如，`* * * * * *`代表每秒执行一次。
- **`,`**：列出多个值。例如，`0 0 10,14,16 * * *`表示每天的10点、14点和16点各执行一次。
- **`-`**：表示一个范围。例如，`0 0 10-12 * * *`表示每天的10、11和12点整执行。
- **`/`**：表示增量。例如，`0 */5 * * * *`表示每隔5分钟执行一次。

### 具体示例

- `@Scheduled(cron = "0 0 10 * * *")`：每天上午10:00执行。
- `@Scheduled(cron = "0 0/15 * * * *")`：每15分钟执行一次。
- `@Scheduled(cron = "0 0 0 1 * *")`：每月1日的午夜（00:00）执行。



