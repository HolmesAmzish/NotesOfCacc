# React 项目创建

## CDN 引入

在不使用打包工具（如 Vite、Webpack、Create React App）的前提下，你可以通过 **CDN** 直接引入 React 和 ReactDOM，然后在 HTML 文件中使用 React。

```html
<!-- React 和 ReactDOM CDN（必须使用 development 版本） -->
<script src="https://unpkg.com/react@18/umd/react.development.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js" crossorigin></script>

<!-- Babel（用于解析 JSX） -->
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
```

随后在 `script` 标签添加 React 代码，JSX 是不是浏览器原生支持的语法，所以必须通过 Babel 来转译 `<App />` 这样的语法。

```html
<script type="text/babel">
  // 定义一个简单组件
  function App() {
    return <h1>Hello, React + CDN!</h1>;
  }
  // 渲染组件
  const root = ReactDOM.createRoot(document.getElementById('example'));
  root.render(<App />);
</script>
```

| 项目         | CDN 地址                                                     | 用途                                              |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------- |
| React 核心库 | `https://unpkg.com/react@18/umd/react.development.js`        | 提供 `React` 全局对象，支持定义组件等功能         |
| ReactDOM     | `https://unpkg.com/react-dom@18/umd/react-dom.development.js` | 提供 `ReactDOM` 全局对象，支持将组件渲染到 DOM 上 |
| Babel        | `https://unpkg.com/@babel/standalone/babel.min.js`           | 让浏览器在运行时解析 JSX                          |

由于 unpkg 提供的 CDN 在国内没有节点，可以使用其他镜像的 CDN 提供 react 框架代码

```html
<script src="https://cdn.jsdelivr.net/npm/react@18/umd/react.development.js"></script>
<script src="https://cdn.jsdelivr.net/npm/react-dom@18/umd/react-dom.development.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@babel/standalone/babel.min.js"></script>
```

> [!NOTE]
>
> 在 `file:///` 协议下，浏览器会出于安全考虑 **禁止脚本发出网络请求或模块加载**；因此如果需要预览，至少需要开启 VSCode 的 Live Server 预览插件。

## NPM 脚手架

# React 快速入门

## 创建和嵌套组件

React 组件是构建 React 应用的基本单位，组件可以分为函数组件和类组件。

React 应用程序是由 **组件** 组成的。一个组件是 UI（用户界面）的一部分，它拥有自己的逻辑和外观。组件可以小到一个按钮，也可以大到整个页面。React 组件是返回标签的 JavaScript 函数：

```jsx
function MyButton() {
  return (
    <button>我是一个按钮</button>
  );
}
```

组件嵌套

```jsx
export default function MyApp() {
  return (
    <div>
      <h1>欢迎来到我的应用</h1>
      <MyButton />
    </div>
  );
}
```

`export default` 关键字指定了文件中的主要组件。如果对 JavaScript 某些语法不熟悉，可以参考 [MDN](https://developer.mozilla.org/zh-CN/docs/web/javascript/reference/statements/export) 和 [javascript.info](https://javascript.info/import-export)。

> [!note]
>
> React 组件必须以大蛇式命名，而 HTML 标签是小写字母，两者予以区分。



## 使用 JSX 编写标签

JSX 比 HTML 更加严格。你必须闭合标签，如 `<br />`。你的组件也不能返回多个 JSX 标签。你必须将它们包裹到一个共享的父级中，比如 `<div>...</div>` 或使用空的 `<>...</>` 包裹：

```jsx
function AboutPage() {
  return (
    <>
      <h1>关于</h1>
      <p>你好。<br />最近怎么样？</p>
    </>
  );
}
```

## 显示数据

JSX 会让你把标签放到 JavaScript 中。而大括号会让你 “回到” JavaScript 中，这样你就可以从你的代码中嵌入一些变量并展示给用户。例如，这将显示 `user.name`：

```jsx
return (
  <h1>
    {user.name}
  </h1>
);
```

你还可以将 JSX 属性 “转义到 JavaScript”，但你必须使用大括号 **而非** 引号。例如，`className="avatar"` 是将 `"avatar"` 字符串传递给 `className`，作为 CSS 的 class。但 `src={user.imageUrl}` 会读取 JavaScript 的 `user.imageUrl` 变量，然后将该值作为 `src` 属性传递：

```jsx
return (
  <img
    className="avatar"
    src={user.imageUrl}
  />
);
```

## 渲染列表

依赖 JavaScript 的特性，例如 [`for` 循环](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/for) 和 [array 的 `map()` 函数](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/map) 来渲染组件列表。

```jsx
const products = [
  { title: 'Cabbage', id: 1 },
  { title: 'Garlic', id: 2 },
  { title: 'Apple', id: 3 },
];
```

在你的组件中，使用 `map()` 函数将这个数组转换为 `<li>` 标签构成的列表:

```jsx
const listItems = products.map(product =>
  <li key={product.id}>
    {product.title}
  </li>
);

return (
  <ul>{listItems}</ul>
);
```

## 响应事件

通过在组件中声明 **事件处理** 函数来响应事件：

```jsx
function MyButton() {
  function handleClick() {
    alert('You clicked me!');
  }

  return (
    <button onClick={handleClick}>
      点我
    </button>
  );
}
```

> [!NOTE]
>
> `onClick={handleClick}` 的结尾没有小括号！不要 **调用** 事件处理函数：你只需 **把函数传递给事件** 即可。`onClick`是事件的触发方式，当用户点击按钮时 React 会调用你传递的事件处理函数。类似于 QT 中的事件绑定。

## 更新界面

通常你会希望你的组件 “记住” 一些信息并展示出来，比如一个按钮被点击的次数。要做到这一点，你需要在你的组件中添加 **state**。

首先，从 React 引入 [`useState`](https://zh-hans.react.dev/reference/react/useState)：

```jsx
import { useState } from 'react';
```

```jsx
function MyButton() {
  const [count, setCount] = useState(0);
  // ...
```

你将从 `useState` 中获得两样东西：当前的 state（`count`），以及用于更新它的函数（`setCount`）。你可以给它们起任何名字，但按照惯例会像 `[something, setSomething]` 这样为它们命名。

第一次显示按钮时，`count` 的值为 `0`，因为你把 `0` 传给了 `useState()`。当你想改变 state 时，调用 `setCount()` 并将新的值传递给它。点击该按钮计数器将递增：

```jsx
function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      Clicked {count} times
    </button>
  );
}
```

React 将再次调用你的组件函数。第一次 `count` 变成 `1`。接着点击会变成 `2`。继续点击会逐步递增。