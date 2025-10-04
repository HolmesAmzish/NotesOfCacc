# JS 的运行环境

## Node.js

使用包管理器安装，nodejs 和 npm （包管理工具）。

```bash
sudo apt update
sudo apt install nodejs npm
```

测试是否安装完成

```bash
node -v
npm -v
```

测试程序，输入 `node` 进入 node 控制台，然后编辑脚本：

```js
console.log("Hello, Node.js!");
```

## npm 包管理

```bash
npm install <package>
```

Node Version Manager (nvm) 安装

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

设置当前配置文件（默认已经添加）

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

加载文件

```bash
source ~/.zshrc
```

验证

```bash
nvm --version
```

