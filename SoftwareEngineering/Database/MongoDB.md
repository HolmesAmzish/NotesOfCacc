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

## **MongoDB Cheat Sheet**

### **1. Basic Commands**

```
# Start Mongo shell
mongo

# Show databases
show dbs

# Use a database (creates if not exists)
use myDatabase

# Show collections in the current DB
show collections

# Drop a database
db.dropDatabase()

# Drop a collection
db.collectionName.drop()
```

------

### **2. CRUD Operations**

#### **Create**

```
// Insert a single document
db.users.insertOne({ name: "Alice", age: 25 })

// Insert multiple documents
db.users.insertMany([
  { name: "Bob", age: 30 },
  { name: "Charlie", age: 28 }
])
```

#### **Read**

```
// Find all documents
db.users.find()

// Pretty print
db.users.find().pretty()

// Find with condition
db.users.find({ age: { $gt: 25 } })

// Find one document
db.users.findOne({ name: "Alice" })

// Count documents
db.users.countDocuments({ age: { $gt: 25 } })
```

#### **Update**

```
// Update one document
db.users.updateOne(
  { name: "Alice" }, 
  { $set: { age: 26 } }
)

// Update multiple documents
db.users.updateMany(
  { age: { $lt: 30 } }, 
  { $inc: { age: 1 } }   // Increment age by 1
)

// Replace a document
db.users.replaceOne({ name: "Alice" }, { name: "Alice", age: 27 })
```

#### **Delete**

```
// Delete one document
db.users.deleteOne({ name: "Bob" })

// Delete multiple documents
db.users.deleteMany({ age: { $lt: 30 } })
```

------

### **3. Query Operators**

#### **Comparison**

```
$eq      // equal
$ne      // not equal
$gt      // greater than
$gte     // greater than or equal
$lt      // less than
$lte     // less than or equal
$in      // in array
$nin     // not in array
```

#### **Logical**

```
$and
$or
$not
$nor
```

#### **Element**

```
$exists  // field exists
$type    // field type
```

#### **Array**

```
$size      // array length
$all       // match all elements
$elemMatch // match array of documents
$push      // add element
$pop       // remove first/last element
```

------

### **4. Aggregation**

```
// Basic aggregation pipeline
db.orders.aggregate([
  { $match: { status: "shipped" } },
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } }
])

// Count documents using aggregation
db.orders.aggregate([
  { $group: { _id: null, count: { $sum: 1 } } }
])
```

------

### **5. Indexing**

```
// Create an index
db.users.createIndex({ name: 1 })       // ascending
db.users.createIndex({ age: -1 })       // descending

// Create a compound index
db.users.createIndex({ name: 1, age: -1 })

// Drop an index
db.users.dropIndex("name_1")
```

------

### **6. Useful Commands**

```
// Show indexes
db.users.getIndexes()

// Explain query plan
db.users.find({ age: { $gt: 25 } }).explain()

// Count all documents in a collection
db.users.estimatedDocumentCount()

// Distinct values
db.users.distinct("name")
```

------

### **7. Data Types**

- **String**: `"hello"`
- **Integer**: `42`
- **Double**: `3.14`
- **Boolean**: `true / false`
- **Array**: `[1, 2, 3]`
- **Object**: `{ key: value }`
- **Date**: `ISODate("2025-08-23T12:00:00Z")`
- **Null**: `null`
- **ObjectId**: `ObjectId("507f191e810c19729de860ea")`
