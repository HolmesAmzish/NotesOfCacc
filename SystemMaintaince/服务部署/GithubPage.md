# GitHub Page 托管博客

GitHub Page 允许托管一份静态网页，而这大大降低了开发者创建一个自己管理博客的成本，尤其是云服务器和带宽等费用。在这里介绍如何用 GitHub Page 部署一份自己的博客网站。最终成果可以参照我的博客 [ArOrms Blog](blog.arorms.cn)。

## GitHub 设置

### 源代码仓库

GitHub Page 允许托管静态网页在 GitHub 服务器上。开发者首先需要以自己的用户名和 GitHub 固定的域名来创建命名一个仓库，例如我的 GitHub 用户名为 holmesamzish，那么创建的仓库名称为 `holmesamzish.github.io`。如果你希望以其他名称命名仓库，比如名称为 `my-blog`，那么最终静态网站托管的地址会在 `username.github.io/my-blog`，所以最简单的方式是默认的设置为自己的用户名。

在仓库中的静态网页代码，就被托管到了 `github.io` 上，如果是以用户名命名的仓库，访问地址在 `username.github.io`，如果仓库名没有使用默认的用户名为名称，则访问地址在 `username.github.io/repository-name`。

### 域名设置

设置后静态页面仓库的访问地址为 `username.github.io`，如果需要更改，通过别名域名解析来访问这个地址也可以。例如我为我的个人博客域名分配为 `blog.arorms.cn`。

首先需要在域名管理中设置解析记录，类型为别名，比如我设置的记录为 `blog.arorms.cn` 解析为 `holmesamzish.arorms.cn`。

其次需要在 GitHub 中验证域名。设置域名解析后无法直接访问 GitHub Page，需要在 GitHub 的 Setting 中，找到 Pages 一栏，有 Verified domains 这里 Add a domain 也就是添加域名的按钮。这里需要你验证添加的域名为你所有，需要按照 GitHub 的提示，设置主机记录为指定的一长串，解析类型为 TXT ，并存放指定字符串。在域名管理系统设置完成后回到 GitHub 验证即可。此时别名就添加完毕了。

### 静态网页生成工具

GitHub Page 仅允许添加静态页面，比较适合存放博客等内容。一般开发者会通过 Markdown 格式记录笔记和博客，可以以 Markdown 文件作为源文件，再利用工具生成静态博客网站，并交付给 GitHub 托管。推荐的工具有 Hugo、Hexo 和 Jekylle。这三款工具各有特点。本文以 Hexo 为例。

## Hexo

### 安装

Hexo 是利用 node.js 编写的，首先需要下载 node.js 环境才可以。在官网下载完成后验证。

```bash
node -v
npm -v
```

随后安装 Hexo CLI

```bash
npm install -g hexo-cli
```

### 创建仓库

```bash
hexo init
```

在 Hexo 初始化后，会在目录 `/source/_posts` 自动生成一篇 Hello World 的文章，文件名为 `hello-world.md` 所以可以直接用这篇文章来测试是否部署完成。可以首先查看一下文章内容。

````markdown
---
title: Hello World
---
Welcome to [Hexo](https://hexo.io/)! This is your very first post. Check [documentation](https://hexo.io/docs/) for more info. If you get any problems when using Hexo, you can find the answer in [troubleshooting](https://hexo.io/docs/troubleshooting.html) or you can ask me on [GitHub](https://github.com/hexojs/hexo/issues).

## Quick Start

### Create a new post

``` bash
$ hexo new "My New Post"
```
......
````

这里 Markdown 的注释 `title` 字段会被 Hexo 认定为这篇文章的标题。

### 运行网站

首先生成静态文件

```bash
hexo generate
```

然后运行服务器

```bash
hexo server
```

运行后通过浏览器访问，地址默认为 `http://localhost:4000`。

### 部署仓库

以上为本地利用 Hexo 生成静态网站访问的方法，需要利用 Hexo 将静态网站托管到 GitHub Page 还需要另外使用对应工具。

```bash
npm install hexo-deployer-git --save
```

随后需要配置根目录下的 `_config.yml` 文件，找到 `deploy` 部分并修改：

```yaml
deploy:
  type: git
  repo: https://github.com/<username>/<repostory-name>.git
  branch: main
```

随后清空之前生成的静态文件，再次生成并部署到 GitHub 上，这里部署会和提交 Git 记录一样显示你所做的更改。

```bash
hexo clean
hexo generate
hexo deploy
```

### 修改设置

大部分设置都在根目录下的 `_config.yml` 文件里，包括网站名和作者。

如果想要更改主题，那么需要在根目录下的 `themes` 文件夹中下载对应的主题文件并在 `_config.yml` 中更改。这里以黑白主题的 NexT 主题为例，首先在 `themes` 文件夹下克隆这个主题：

```bash
git clone --depth 1 https://github.com/next-theme/hexo-theme-next.git next
```

克隆完成后在 `_config.yml` 文件中修改 theme 字段

```yaml
# Extensions
## Plugins: https://hexo.io/plugins/
## Themes: https://hexo.io/themes/
theme: next
```

如果有数学公式编写，需要解析 LaTex 数学公式需要开启 MathJax。在 `themes/next/_config.yml` 文件下，找到如下字段并更改。

```yaml
math:
  # Default (false) will load mathjax / katex script on demand.
  # That is it only render those page which has `mathjax: true` in front-matter.
  # If you set it to true, it will load mathjax / katex script EVERY PAGE.
  every_page: true

  mathjax:
    enable: true
    # Available values: none | ams | all
    tags: none

  katex:
    enable: false
    # See: https://github.com/KaTeX/KaTeX/tree/master/contrib/copy-tex
    copy_tex: false
```

更改后重新部署即可发现渲染出数学公式。

