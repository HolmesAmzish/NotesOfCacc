---
title: MongoDB 数据库操作
date: 2025-05-08
author: Cacc
---

# MongoDB 数据库操作

```shell
db.<collection_name>.find({"name":""})
```

在 MongoDB 中，导入导出数据主要使用以下几个工具命令：

------

## 🟩 一、导出数据（从 MongoDB 导出到 JSON/CSV）

MongoDB 提供了 `mongoexport` 工具。

### ✅ 1. 导出为 JSON 文件

```bash
mongoexport --db=<数据库名> --collection=<集合名> --out=<输出文件路径>.json
```

🔸 示例：

```bash
mongoexport --db=mydb --collection=users --out=users.json
```

### ✅ 2. 导出为 CSV 文件（需指定字段）

```bash
mongoexport --db=<数据库名> --collection=<集合名> --type=csv --fields=<字段列表> --out=<文件名>.csv
```

🔸 示例：

```bash
mongoexport --db=mydb --collection=users --type=csv --fields=name,email,age --out=users.csv
```

------

## 🟦 二、导入数据（从 JSON/CSV 文件导入到 MongoDB）

使用 `mongoimport` 工具。

### ✅ 1. 从 JSON 文件导入

```bash
mongoimport --db=<数据库名> --collection=<集合名> --file=<文件名>.json --jsonArray
```

> ```
> --jsonArray` 适用于整个 JSON 是数组形式的文件，比如 `[ {...}, {...} ]
> ```

🔸 示例：

```bash
mongoimport --db=mydb --collection=users --file=users.json --jsonArray
```

### ✅ 2. 从 CSV 文件导入

```bash
mongoimport --db=<数据库名> --collection=<集合名> --type=csv --headerline --file=<文件名>.csv
```

🔸 示例：

```bash
mongoimport --db=mydb --collection=users --type=csv --headerline --file=users.csv
```

------

## 🧰 三、一些常用参数说明

| 参数           | 说明                                   |
| -------------- | -------------------------------------- |
| `--uri`        | 指定连接字符串（如远程 MongoDB Atlas） |
| `--db`         | 数据库名称                             |
| `--collection` | 集合名称                               |
| `--file`       | 导入/导出文件路径                      |
| `--jsonArray`  | 指定 JSON 文件是数组格式               |
| `--fields`     | 导出时选择字段                         |
| `--type`       | 文件类型（json 或 csv）                |
| `--headerline` | CSV 第一行是字段名（用于导入）         |

------

## 🧪 示例文件格式（导入时）

### JSON 示例（需要 `--jsonArray`）：

```json
[
  { "name": "Alice", "age": 25 },
  { "name": "Bob", "age": 30 }
]
```

### CSV 示例：

```csv
name,email,age
Alice,alice@example.com,25
Bob,bob@example.com,30
```

------

## 🖥️ 检查工具是否可用

这些命令行工具通常位于 MongoDB 安装目录的 `bin` 文件夹中，例如：

- Windows：`C:\Program Files\MongoDB\Server\<version>\bin`
- Linux/macOS：可能已全局安装（可直接运行）

你可以通过命令确认是否可用：

```bash
mongoexport --version
mongoimport --version
```

------

如需我帮你写一个导入导出的完整脚本，或你用的是 MongoDB Atlas、Docker、GUI 工具（如 Compass），也可以告诉我，我来补充。
