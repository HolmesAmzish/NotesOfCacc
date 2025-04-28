---
title: Electron intro
author: Cacciatore
date: 2025-03-27 19:48
---



# Electron 介绍

## 技术栈

Web 技术包括 HTML、CSS、JavaScript 和 WebAssembly。 它们是现代互联网的基石。  这些技术已成为构建用户界面的最佳选择——无论是对于消费者应用程序还是关键业务型应用程序。  这不仅适用于需要在浏览器中运行的应用程序，也适用于那些无法通过浏览器访问的桌面应用程序。  我们在此大胆断言，这不仅适用于需要在多个操作系统上运行的跨平台应用程序，而且适用于所有类型的应用程序。

Electron 是一个框架，使开发者能够将 Web 技术(HTML、JavaScript、CSS)、Node.js  及原生代码相结合，构建适用于 macOS、Windows 和 Linux 的跨平台桌面应用程序。  它基于MIT开源许可证，对商业和个人用途均免费。Electron 将 Chromium、Node.js 和编写自定义原生代码的能力结合到一个框架中，用于构建强大的桌面应用程序。 

## 环境需求

要开发 Electron 应用，您需要安装 [Node.js](https://nodejs.org/en/download/) 运行环境和它的包管理器 npm。 我们推荐安装最新的长期支持 (LTS) 版本。检查 node.js 是否安装。

```bash
$ node -v
v16.14.2
$ npm -v
8.7.0
```

> [!NOTE]
>
> 虽然您需要在开发环境安装 Node.js 才能编写 Electron 项目，但是 Electron **不使用您系统的 Node.js 环境来运行它的代码**。 相反地，它使用它内置的 Node.js 运行时。 这意味着您的终端用户不需要 Node.js 环境也可以运行您的应用。

## 创建 Electron 项目

### 初始化 npm 项目

Electron 应用基于 npm 搭建，以 package.json 文件作为入口点。 首先创建一个文件夹，然后在其中执行 `npm init` 初始化项目。

```bash
mkdir my-electron-app && cd my-electron-app
npm init
```

这条命令会帮您配置 package.json 中的一些字段。 为本教程的目的，有几条规则需要遵循：

- *入口点* 应当是 `main.js` (您很快就会创建它)
- *author*、*license* 和 *description* 可以是任何值，但在稍后的[packaging](https://www.electronjs.org/zh/docs/latest/tutorial/打包教程)中是必需的。

然后，将 Electron 安装为您项目的 **devDependencies**，即仅在开发环境需要的额外依赖。

```bash
npm install electron --save-dev
```

在初始化并且安装完 Electron 之后，您的 package.json 应该长下面这样。 文件夹中会出现一个 `node_modules` 文件夹，其中包含了 Electron 可执行文件；还有一个 `package-lock.json` 文件，指定了各个依赖的确切版本。

package.json

```json
{
  "name": "my-electron-app",
  "version": "1.0.0",
  "description": "Hello World!",
  "main": "main.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "Jane Doe",
  "license": "MIT",
  "devDependencies": {
    "electron": "23.1.3"
  }
}
```



### 添加 .gitignore 文件

[`.gitignore`](https://git-scm.com/docs/gitignore) 文件可以指定哪些文件和目录应该在Git中不被跟踪。 建议您复制一份 [GitHub 的 Node.js gitignore 模板](https://github.com/github/gitignore/blob/main/Node.gitignore) 到您项目的根目录，以避免将 `node_modules` 文件夹提交到版本控制系统中。

## 运行 Electron 应用

您在 package.json 中指定的 [`main`](https://docs.npmjs.com/cli/v7/configuring-npm/package-json#main) 文件是 Electron 应用的入口。 这个文件控制 **主程序 (main process)**，它运行在 Node.js 环境里，负责控制您应用的生命周期、显示原生界面、执行特殊操作并管理渲染器进程 (renderer processes)，稍后会详细介绍。

在继续编写您的 Electron 应用之前，您将使用一个小小的脚本来确保主进程入口点已经配置正确。 在根目录的 `main.js` 文件中写一行代码：

main.js

```js
console.log('Hello from Electron 👋')
```

因为 Electron 的主进程就是一个 Node.js 运行时，所以你可以直接用 `electron` 命令运行任意的 Node.js 代码（甚至还能把它当成 [REPL](https://www.electronjs.org/zh/docs/latest/tutorial/repl) 来用）。 要执行这个脚本，需要在 package.json 的 [`scripts`](https://docs.npmjs.com/cli/v7/using-npm/scripts) 字段中添加一个 `start` 命令，内容为 `electron .` 。 这个命令会告诉 Electron 在当前目录下寻找主脚本，并以开发模式运行它。

package.json

```json
{
  "name": "my-electron-app",
  "version": "1.0.0",
  "description": "Hello World!",
  "main": "main.js",
  "scripts": {
    "start": "electron .",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "Jane Doe",
  "license": "MIT",
  "devDependencies": {
    "electron": "23.1.3"
  }
}
```

```sh
npm run start
```

您的终端应该会输出 `欢迎来到 Electron 👋`。 恭喜，您已经在 Electron 中执行了您的第一行代码！ 接下来，您会学习如何用 HTML 创建用户界面，并将它们装载到原生窗口中。

## BrowserWindow

在 Electron 中，每个窗口展示一个页面，后者可以来自本地的 HTML，也可以来自远程 URL。 在本例中，您将会装载本地的文件。 在您项目的根目录中创建一个 `index.html` 文件，并写入下面的内容：

index.html

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP -->
    <meta
      http-equiv="Content-Security-Policy"
      content="default-src 'self'; script-src 'self'"
    />
    <meta
      http-equiv="X-Content-Security-Policy"
      content="default-src 'self'; script-src 'self'"
    />
    <title>Hello from Electron renderer!</title>
  </head>
  <body>
    <h1>Hello from Electron renderer!</h1>
    <p>👋</p>
  </body>
</html>
```

现在您有了一个网页，您可以将其加载到一个 Electron 的 [BrowserWindow](https://www.electronjs.org/zh/docs/latest/api/browser-window) 上了。 将 `main.js` 中的内容替换成下列代码。 我们马上会逐行解释。

main.js

```js
const { app, BrowserWindow } = require('electron')

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600
  })

  win.loadFile('index.html')
}

app.whenReady().then(() => {
  createWindow()
})
```

### 导入模块

main.js (Line 1)

```js
const { app, BrowserWindow } = require('electron')
```

在第一行中，我们使用 CommonJS 语法导入了两个 Electron 模块：

- [app](https://www.electronjs.org/zh/docs/latest/api/app)，这个模块控制着您应用程序的事件生命周期。
- [BrowserWindow](https://www.electronjs.org/zh/docs/latest/api/browser-window)，这个模块创建和管理 app 的窗口。

<details class="details_lb9f isBrowser_bmU9 alert alert--info details_b_Ee" data-collapsed="true"><summary>模块名的大小写规范</summary></details>

<details class="details_lb9f isBrowser_bmU9 alert alert--info details_b_Ee" data-collapsed="true"><summary>类型化导入别名</summary></details>



Electron 中的 ES 模块

Electron 28 起，Electron 支持[ECMAScript 模块](https://nodejs.org/api/esm.html)（即使用 `import` 加载模块）。 您可以在我们的 [ESM 指南](https://www.electronjs.org/zh/docs/latest/tutorial/esm) 中找到有关 Electron 中 ESM 状态以及如何在我们的应用程序中使用它们的更多信息。

### 实例化窗口

`createWindow()` 函数将您的页面加载到新的 BrowserWindow 实例中：

**main.js (Lines 3-10)**

```js
const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600
  })

  win.loadFile('index.html')
}
```

### 调用函数

**main.js (Lines 12-14)**

```js
app.whenReady().then(() => {
  createWindow()
})
```

Electron 的许多核心模块都是 Node.js 的[事件触发器](https://nodejs.org/api/events.html#events)，遵循 Node.js 的异步事件驱动架构。 app 模块就是其中一个。

在 Electron 中，只有在 app 模块的 [`ready`](https://www.electronjs.org/zh/docs/latest/api/app#event-ready) 事件（event）触发后才能创建 BrowserWindows 实例。 您可以通过使用 [`app.whenReady()`](https://www.electronjs.org/zh/docs/latest/api/app#appwhenready) API 来监听此事件，并在其成功后调用 `createWindow()` 方法。



info

通常我们使用触发器的 `.on` 函数来监听 Node.js 事件。

```diff
+ app.on('ready', () => {
- app.whenReady().then(() => {
  createWindow()
})
```

但是 Electron 暴露了 `app.whenReady()` 方法，作为其 `ready` 事件的专用监听器，这样可以避免直接监听 .on 事件带来的一些问题。 参见 [electron/electron#21972](https://github.com/electron/electron/pull/21972) 。

此时，运行 `start` 命令应该能成功地打开一个包含您网页内容的窗口！

您应用中的每个页面都在一个单独的进程中运行，我们称这些进程为 **渲染器 (\*renderer\*)** 。 渲染进程使用与常规Web开发相同的JavaScript API和工具，例如使用 [webpack](https://webpack.js.org)来打包和压缩您的代码，或使用 [React](https://reactjs.org) 构建用户界面。

## 应用的生命周期

应用窗口在不同操作系统中的行为也不同。 Electron 允许您自行实现这些行为来遵循操作系统的规范，而不是采用默认的强制执行。 您可以通过监听 app 和 BrowserWindow 模组的事件，自行实现基础的应用窗口规范。



针对特定进程的控制流

通过检查 Node.js 的 [`process.platform`](https://nodejs.org/api/process.html#process_process_platform) 变量，您可以针对特定平台运行特定代码。 请注意，Electron 目前只支持三个平台：`win32` (Windows), `linux` (Linux) 和 `darwin` (macOS) 。

### 关闭窗口退出应用

在 Windows 和 Linux 上，我们通常希望在关闭一个应用的所有窗口后让它退出。 要在您的Electron应用中实现这一点，您可以监听 app 模块的 [`window-all-closed`](https://www.electronjs.org/zh/docs/latest/api/app#event-window-all-closed) 事件，并在判断用户不使用 macOS 后调用 [`app.quit()`](https://www.electronjs.org/zh/docs/latest/api/app#appquit) 来退出您的应用程序。

```js
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})
```

### 打开另一个窗口

与前二者相比，即使没有打开任何窗口，macOS 应用通常也会继续运行。 在没有窗口可用时调用 app 会打开一个新窗口。

要实现这一特性，可以监听 app 模组的 [`activate`](https://www.electronjs.org/zh/docs/latest/api/app#event-activate-macos) 事件，如果没有任何打开（open）的 BrowserWindow，调用您已有的`createWindow()` 方法新建一个。

因为窗口无法在 `ready` 事件前创建，你应当在你的应用初始化后仅监听 `activate` 事件。 要实现这个，仅监听 `whenReady()` 回调即可。

```js
app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})
```



---

# Electron 中的流程

## 流程模型

Electron 继承了来自 Chromium 的多进程架构，这使得此框架在架构上非常相似于一个现代的网页浏览器。 

### 多进程模型

为了解决这个问题，Chrome 团队决定让每个标签页在自己的进程中渲染， 从而限制了一个网页上的有误或恶意代码可能导致的对整个应用程序造成的伤害。 然后用单个浏览器进程控制这些标签页进程，以及整个应用程序的生命周期。



<img src="https://www.electronjs.org/zh/assets/images/chrome-processes-0506d3984ec81aa39985a95e7a29fbb8.png" width=80%>

Electron 应用程序的结构非常相似。 作为应用开发者，你将控制两种类型的进程：[主进程](https://www.electronjs.org/zh/docs/latest/tutorial/process-model#the-main-process) 和 [渲染器进程](https://www.electronjs.org/zh/docs/latest/tutorial/process-model#the-renderer-process)。 这类似于上文所述的 Chrome 的浏览器和渲染器进程。

### 主进程

每个 Electron 应用都有一个单一的主进程，作为应用程序的入口点。 主进程在 Node.js 环境中运行，这意味着它具有 `require` 模块和使用所有 Node.js API 的能力。

`BrowserWindow` 类的每个实例创建一个应用程序窗口，且在单独的渲染器进程中加载一个网页。

```js
const { BrowserWindow } = require('electron')

const win = new BrowserWindow({ width: 800, height: 1500 })
win.loadURL('https://github.com')

const contents = win.webContents
console.log(contents)
```

由于 `BrowserWindow` 模块是一个 [`EventEmitter`](https://nodejs.org/api/events.html#events_class_eventemitter)， 所以您也可以为各种用户事件 ( 例如，最小化 或 最大化您的窗口 ) 添加处理程序。

当一个 `BrowserWindow` 实例被销毁时，与其相应的渲染器进程也会被终止。

### 渲染器进程

每个 Electron 应用都会为每个打开的 `BrowserWindow` ( 与每个网页嵌入 ) 生成一个单独的渲染器进程。 洽如其名，渲染器负责 *渲染* 网页内容。 所以实际上，运行于渲染器进程中的代码是须遵照网页标准的 (至少就目前使用的 Chromium 而言是如此) 。

因此，一个浏览器窗口中的所有的用户界面和应用功能，都应与您在网页开发上使用相同的工具和规范来进行攥写。

### Preload 脚本

预加载（preload）脚本包含了那些执行于渲染器进程中，且先于网页内容开始加载的代码 。 这些脚本虽运行于渲染器的环境中，却因能访问 Node.js API 而拥有了更多的权限。

预加载脚本可以在 `BrowserWindow` 构造方法中的 `webPreferences` 选项里被附加到主进程。

main.js

```js
const { BrowserWindow } = require('electron')
// ...
const win = new BrowserWindow({
  webPreferences: {
    preload: 'path/to/preload.js'
  }
})
// ...
```

因为预加载脚本与浏览器共享同一个全局 [`Window`](https://developer.mozilla.org/en-US/docs/Web/API/Window) 接口，并且可以访问 Node.js API，所以它通过在全局 `window` 中暴露任意 API 来增强渲染器，以便你的网页内容使用。

preload.js

```js
window.myAPI = {
  desktop: true
}
```

renderer.js

```js
console.log(window.myAPI)
// => undefined
```

语境隔离（Context Isolation）意味着预加载脚本与渲染器的主要运行环境是隔离开来的，以避免泄漏任何具特权的 API 到您的网页内容代码中。

Instead, use the [`contextBridge`](https://www.electronjs.org/zh/docs/latest/api/context-bridge) module to accomplish this securely:

preload.js

```js
const { contextBridge } = require('electron')

contextBridge.exposeInMainWorld('myAPI', {
  desktop: true
})
```

renderer.js

```js
console.log(window.myAPI)
// => { desktop: true }
```

## 上下文隔离

### 上下文隔离是什么？

上下文隔离功能将确保您的 `预加载`脚本 和 Electron的内部逻辑 运行在所加载的 [`webcontent`](https://www.electronjs.org/zh/docs/latest/api/web-contents)网页 之外的另一个独立的上下文环境里。  这对安全性很重要，因为它有助于阻止网站访问 Electron 的内部组件 和 您的预加载脚本可访问的高等级权限的API 。

这意味着，实际上，您的预加载脚本访问的 `window` 对象**并不是**网站所能访问的对象。  例如，如果您在预加载脚本中设置 `window.hello = 'wave'` 并且启用了上下文隔离，当网站尝试访问`window.hello`对象时将返回 undefined。

自 Electron 12 以来，默认情况下已启用上下文隔离，并且它是 _所有应用程序_推荐的安全设置。

### 与Typescript一同使用

如果您正在使用 TypeScript 构建 Electron 应用程序，您需要给通过 context bridge 暴露的 API 添加类型。 渲染进程的 `window` 对象将不会包含正确扩展类型，除非给其添加了 [类型声明](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html)。

例如，在这个 `preload.ts` 脚本中：

preload.ts

```ts
contextBridge.exposeInMainWorld('electronAPI', {
  loadPreferences: () => ipcRenderer.invoke('load-prefs')
})
```

您可以创建一个 `interface.d.ts` 类型声明文件，并且全局增强 `Window` 接口。

interface.d.ts

```ts
export interface IElectronAPI {
  loadPreferences: () => Promise<void>,
}

declare global {
  interface Window {
    electronAPI: IElectronAPI
  }
}
```

以上所做皆是为了确保在您编写渲染进程的脚本时， TypeScript 编译器将会知晓`electronAPI`合适地在您的全局`window`对象中

renderer.ts

```ts
window.electronAPI.loadPreferences()
```

# 进程间通信 

进程间通信 (IPC) 是在 Electron 中构建功能丰富的桌面应用程序的关键部分之一。 由于主进程和渲染器进程在 Electron  的进程模型具有不同的职责，因此 IPC 是执行许多常见任务的唯一方法，例如从 UI 调用原生 API 或从原生菜单触发 Web 内容的更改。