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

