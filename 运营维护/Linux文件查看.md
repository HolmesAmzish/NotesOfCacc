# Linux 文件分析工具组合技笔记

## 1. 基础命令速览（不解释用法）

```bash
cat     # 连接并显示文件内容
grep    # 基于正则表达式的行筛选
sort    # 行排序（支持复杂排序逻辑）
uniq    # 去重
wc      # 统计行、字、字符数
cut     # 按列提取
awk     # 高级字段处理
sed     # 流编辑器，支持替换、删除、插入
```

------

## 2. 典型用法组合

### 2.1 提取包含“ERROR”的日志行并排序去重

```bash
cat app.log | grep "ERROR" | sort | uniq
```

### 2.2 按时间戳字段排序日志（假设格式为 `YYYY-MM-DD HH:MM:SS ...`）

```bash
cat app.log | sort -k1,2
```

### 2.3 统计每种错误类型出现次数（假设以“[ERROR_TYPE]”格式出现）

```bash
grep "\[.*\]" app.log | cut -d'[' -f2 | cut -d']' -f1 | sort | uniq -c | sort -nr
```

------

## 3. 正则表达式高级用法（grep -E）

### 3.1 匹配包含邮箱地址的行

```bash
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}" users.txt
```

### 3.2 匹配 IP 地址格式的行

```bash
grep -E "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" logs.txt
```

### 3.3 查找以数字开头、包含特定关键字的行

```bash
grep -E "^[0-9].*timeout" server.log
```

------

## 4. 综合实例：分析访问日志

### 假设 `access.log` 格式如下：

```
192.168.0.1 - - [10/May/2025:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 1024
```

### 4.1 提取所有访问 IP 并统计访问次数

```bash
cut -d' ' -f1 access.log | sort | uniq -c | sort -nr
```

### 4.2 统计请求状态码分布

```bash
awk '{print $9}' access.log | sort | uniq -c | sort -nr
```

### 4.3 统计某天的请求总数（如 2025年5月10日）

```bash
grep "10/May/2025" access.log | wc -l
```

------

## 5. sed 与 awk 的复杂组合应用

### 5.1 sed 替换日志中的私密信息（如邮箱地址）

```bash
sed -E 's/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}/[REDACTED]/g' emails.log
```

### 5.2 awk 分析字段并自定义输出

```bash
awk '{ip=$1; code=$9; bytes=$10; print ip "\t" code "\t" bytes}' access.log
```

### 5.3 awk 按条件统计（统计所有状态码为500的请求数）

```bash
awk '$9 == 500 {count++} END {print count}' access.log
```

------

## 6. 多文件分析与合并

### 6.1 合并多个日志文件并去重排序

```bash
cat logs/*.log | sort | uniq > all.log
```

### 6.2 比较两个文件中独有的行（集合差异）

```bash
comm -3 <(sort file1.txt) <(sort file2.txt)
```

------

## 7. 统计与分析

### 7.1 文件总行数、单词数、字节数

```bash
wc file.txt
```

### 7.2 统计出现次数最多的单词

```bash
tr -s '[:space:]' '\n' < file.txt | grep -v '^$' | sort | uniq -c | sort -nr | head
```

------

## 8. 高级技巧

### 8.1 忽略大小写统计关键词频率

```bash
grep -i "fail" system.log | wc -l
```

### 8.2 仅输出匹配内容（不是整行）

```bash
grep -oE "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}" file.txt
```

### 8.3 多关键词或匹配模式

```bash
grep -E "timeout|refused|unreachable" network.log
```

------

## 9. 性能优化建议

- 使用 `LC_ALL=C sort` 加快排序
- 使用 `--binary-files=text` 强制处理非文本日志
- 管道前加 `stdbuf -oL` 实现实时流处理



# 示例

```bash
sort give_data/4_give.txt | grep -E '.+:.+:.+:.+:.+:.+:.+:.+' > 4_long.txt
sort give_data/4_give.txt | grep b'.+:.+:.+:.+:.+:.+:.+:.+' > 4_long.txt
```

```bash
```

