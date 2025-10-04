---
title: Express.js 基础
author: Cacciatore
date: 2025-07-05
---

首先下载 node.js 环境并通过 node.js 对 Express 依赖进行管理

```bash
mkdir express_demo && cd express_demo
npm init -y
npm install express
```

利用 express 创建 app 实例并开启监听，成功即打印信息

**index.js**

```js
const express = require('express');
const app = express();
const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
```

```bash
node index.js
```

输出：

```
Server is running on http://localhost:3000
```

添加 GET 方法 API

```js
app.get("/data", (req, res) => {
    console.log("Received a request for /data: ", req.query);
    res.json({ message: "Hello, World!" });
});
```

重启后的输出

```
Received a request for /data:  [Object: null prototype] { username: 'cacc' }
```



中间件通过中间包装实现对应的对 app 实例操作的更改，添加依赖后

```js
app.use(express.json());
app.use(cors());
```

这两个中间件实现了对接收回应请求实体的对象化以及跨域处理的解决。



静态文件托管

```js
app.use(express.static(path.join(__dirname, 'public')));
```

同时创建 public 文件夹，即可直接访问 public 文件夹下的静态资源。