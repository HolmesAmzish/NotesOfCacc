# JavaScript 基础

## 基本语法

### 数据类型

#### 映射

```js
let names = ['Michael', 'Bob', 'Tracy'];
let scores = [95, 75, 85];

let m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);
m.get('Michael'); // 95
```



### 输出

```js
console.log("Hello, World!");

alert('Hello');

// This is a comment
```



### 字符串

```js
let s = 'Hello, world!';
s.length;
```



## 对象

### 对象的创建与操作

在 JS 中，一个对象由多个成员组成，语法规则如下

```js
const objectName = {
  member1Name: member1Value,
  member2Name: member2Value,
  member3Name: member3Value,
};
```

例子：

```js
const person = {
  name: ["Bob", "Smith"],
  age: 32,
  bio: function () {
    console.log(`${this.name[0]} ${this.name[1]} 现在 ${this.age} 岁了。`);
  },
  introduceSelf: function () {
    console.log(`你好！我是 ${this.name[0]}。`);
  },
};
```

其中， `bio()` 可以用来代替 `bio: function()`

```js
bio() {
  console.log(`${this.name[0]} ${this.name[1]} 现在 ${this.age} 岁了。`);
},
```

### this

```js
const person1 = {
  name: "Chris",
  introduceSelf() {
    console.log(`你好！我是 ${this.name}。`);
  },
};

const person2 = {
  name: "Deepti",
  introduceSelf() {
    console.log(`你好！我是 ${this.name}。`);
  },
};
```

### 构造函数

```js
function createPerson(name) {
  const obj = {};
  obj.name = name;
  obj.introduceSelf = function () {
    console.log(`你好！我是 ${this.name}。`);
  };
  return obj;
}
```

```js
const salva = createPerson("Salva");
salva.name;
salva.introduceSelf();
// "你好！我是 Salva。"

const frankie = createPerson("Frankie");
frankie.name;
frankie.introduceSelf();
// "你好！我是 Frankie。"
```



### 预定义

#### Date

```js
let now = new Date();
now;
```

## 异步编程基础







# JS 与浏览器

窗口（window）是载入网页的浏览器标签；在JS中由 `window` 对象表示。

导航器（navigator）在网络上出现时，代表浏览器的状态和身份。在JS中由 `Navigator` 对象表示。

文档（document，在浏览器中用DOM表示）是加载到窗口的实际页面，在 JavaScript 中，由 `Document` 对象表示，可以使用这个对象来返回和操作构成文档的 HTML 和 CSS 的信息。例如在 DOM 中获得一个元素的引用，改变其文本内容，对其应用新的样式，创建新的元素并将其作为子元素添加到当前元素中，甚至完全删除它。

## DOM 操作

### 文档对象模型

```html
<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <title>Simple DOM example</title>
  </head>
  <body>
    <section>
      <img
        src="dinosaur.png"
        alt="A red Tyrannosaurus Rex: A two legged dinosaur standing upright like a human, with small arms, and a large head with lots of sharp teeth." />
      <p>
        Here we will add a link to the
        <a href="https://www.mozilla.org/">Mozilla homepage</a>
      </p>
    </section>
  </body>
</html>
```

其DOM树如下所示

<img src="https://developer.mozilla.org/zh-CN/docs/Learn_web_development/Core/Scripting/DOM_scripting/dom-screenshot.png" width=100%>

> [!TIP]
>
> https://software.hixie.ch/utilities/js/live-dom-viewer/

### 更改节点内容

要操作 DOM 内的元素，首先需要选择它，并将它的引用存储在一个变量中。可以通过 document 对象的 querySelector 方法来查找元素。

```js
const link = document.querySelector("a")
link.textContent = "Mozilla Developer Network";
link.href = "https://developer.mozilla.org";
```

这样就将元素引用存储在一个变量中，这样就可更改他的属性，例如将 `textContent`和`href`更改。

`document.querySelector()`是推荐的现代方法，上面的 `querySelector()` 调用将匹配文档中出现的第一个 `<a>` 元素。除此之外还有 `document.querySelectorAll()`

`document.getElementById()`

`document.getElementByTagName()`

### 创建并放置新的节点

首先获取 `<section>` 元素的引用

```js
const sect = document.querySelector("section");
```

使用 document 对象的方法创建一个新的段落

```js
const para = document.createElement("p");
para.textContent = "We hope you enjoyed the ride.";
```

在父元素的引用添加新的孩子结点

```js
sect.appendChild(para);
```

### 操作样式

通过更改选中的对象的属性来更改样式

```js
para.style.color = "white";
para.style.backgroundColor = "black";
para.style.padding = "10px";
para.style.width = "250px";
para.style.textAlign = "center";
```

或者通过更改类

```html
<style>
  .highlight {
    color: white;
    background-color: black;
    padding: 10px;
    width: 250px;
    text-align: center;
  }
</style>
```

```js
para.setAttribute("class", "highlight");
```





## 表单操作



## 浏览器 API

# 后端交互

## HTTP 基础



## 使用 Fetch API

`fetch`的基本语法

```js
fetch(apiUrl)
	.then(response => response.json())
	.then(data => console.log(data))
	.catch(error => consol.error('Error:', error));
```

`fetch`首先发起请求然后返回一个`response`对象。第二个`then`将`response`对象解析成json数据并返回一个新的 Promise，第二个`then`接收`.json()`方法返回的解析结果并赋值给`data`，然后通过控制台打印出来。最后是异常处理。



## 跨域与 CORS

**跨域（Cross-Origin）** 指的是浏览器出于安全策略（同源策略），限制不同域之间的请求。

**CORS（跨域资源共享，Cross-Origin Resource Sharing）** 是一种允许服务器声明哪些来源可以访问其资源的机制。

服务器需要在 HTTP 响应头中添加 `Access-Control-Allow-Origin` 允许特定来源跨域访问：

```
Access-Control-Allow-Origin: *
```

或指定某个域名：

```
Access-Control-Allow-Origin: https://example.com
```

## WebSocket 简介

WebSocket 允许在客户端和服务器之间建立持久连接，实现实时通信。

示例：

**服务器端（Node.js）**

```js
const WebSocket = require("ws");
const wss = new WebSocket.Server({ port: 8080 });

wss.on("connection", (ws) => {
  ws.send("欢迎连接 WebSocket 服务器");
  ws.on("message", (message) => {
    console.log(`收到消息: ${message}`);
  });
});
```

**客户端**

```js
const socket = new WebSocket("ws://localhost:8080");

socket.onmessage = (event) => {
  console.log("收到消息: ", event.data);
};
```

## 前端调用后端 API

```js
fetch("https://api.example.com/data")
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error("Error:", error));
```



# 模块化与工具

## ES 模块化



## 常用工具库



## 构建工具的简单了解



