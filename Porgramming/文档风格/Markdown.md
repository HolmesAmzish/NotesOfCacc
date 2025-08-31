# Markdown 语法

## 基本语法

| 元素     | Markdown 语法                    |
| -------- | -------------------------------- |
| 标题     | `# H1`                           |
| 粗体     | `**bold text**`                  |
| 斜体     | `*italicized text*`              |
| 删除线   | `~~The world is flat.~~`         |
| 引用块   | `> blockquote`                   |
| 有序列表 | `1. First item` `2. Second item` |
| 无序列表 | `- First item` `- Second item`   |
| 代码     | `` `code` ``                     |
| 分割线   | `---`                            |
| 链接     | `[title](http://website.com)`    |
| 图片     | `![alt text](image.png)`         |

标题可以使用多个井号来进行分级，# 一级标题，## 二级标题，### 三级标题。

## 扩展语法

表格

```markdown
| Syntax	| Decription	|
|-----------|---------------|
| Header	| Title			|
| Paragraph	| Text			|
```

代码块

```cpp
using System;

class Hello{
    static void Main() {
        Console.WriteLine("Hello, World!");
        Console.ReadLine();
    }
}
```

注脚

Here's a sentence with a foot note.`[^1]`

`[^1]`:This is the footnote.

标题编号

`### My Great Heading {#custom-id}`

任务列表

```markdown
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media
```

## 数学公式

Typora 或其他 Markdown 编辑渲染软件可以以 LaTex 语法渲染公式，公式使用 `$$` 开启。大部分软件还支持行内公式，只需要在行内用 `$` 或 `$$` 包裹即可。

```
WS小世界中，重联概率为0时，K个邻居节点之间的边数是 $M_0 = 3K(K - 2)/8$ ，三个节点之间的三条边保持不变的概率为 $(1 - p)^3$ ，发生边的重连和补回的概率为 $1/(N - 1)$ 。邻居节点之间的连边的平均数为 $M_0(1 - p)^3 + O(1/N)$ ，因此WS小世界的聚类系数为
```

WS小世界中，重联概率为0时，K个邻居节点之间的边数是 $$M_0 = 3K(K - 2)/8$$ ，三个节点之间的三条边保持不变的概率为 $$(1 - p)^3$$ ，发生边的重连和补回的概率为 $$1/(N - 1)$$ 。邻居节点之间的连边的平均数为 $$M_0(1 - p)^3 + O(1/N)$$​ ，因此WS小世界的聚类系数为

```latex
$$
\begin{align}
C_{WS} &= \frac{3K(K - 2)/8}{K(K - 1)/2}(1 - p)^3 + O(1/N) \\
&= C_{nc}(1 - p)^3 + O(1/N)
\end{align}
$$
```

$$
\begin{align}
C_{WS} &= \frac{3K(K - 2)/8}{K(K - 1)/2}(1 - p)^3 + O(1/N) \\
&= C_{nc}(1 - p)^3 + O(1/N)
\end{align}
$$

> [!TIP]
>
> 在 Typora 中编辑行内公式需要先开启此功能，一般默认只渲染公式块。



# Typora

## 设置

## 快捷键

Typora 是一款支持 Markdown 编辑和渲染的软件，在编辑 Markdown 的同时还提供了许多快捷键来提高工作效率。

| 功能     | 快捷键           |
| -------- | ---------------- |
| 代码块   | ctrl + shift + k |
| 行内代码 | ctrl + shift + ` |
| 公式     | ctrl + shift + m |

