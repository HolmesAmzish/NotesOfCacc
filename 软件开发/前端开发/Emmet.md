# Emmet

## 自动生成框架

输入`!`或者`html:5`，按下Tab补全框架

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

</body>
</html>
```

其次，还有许多自动补全关键词

`!!!`: `<!DOCTYPE html>`

`html`: `<html></html>`

`html:xml`: `<html xmlns="http://www.w3.org/1999/xhtml"></html>`

## 自动生成注释

按下Ctrl + /自动生成注释

```html
<!--  -->
```

## 自动生成测试文本

输入`lorem`按下Tab生成测试文本

```html
Lorem ipsum dolor, sit amet consectetur adipisicing elit. Perspiciatis, error voluptates incidunt corrupti recusandae fugiat repellendus distinctio beatae sed atque ab ipsam consequatur. Voluptatem, atque expedita quae vitae dolor corporis!
```

## 自动补全

输入标签名直接补全，例如输入`h1`自动补全

```html
<h1></h1>
```

嵌套元素，使用`>`连接，例如输入`ul>li`

```html
<lu>
    <li></li>
</lu>
```

重复标签，例如输入`ul>li*3`

```html
<lu>
    <li></li>
    <li></li>
    <li></li>
</lu>
```

自动补全标签时自带id或类

```html
<!-- 输入 p.content -->
<p class="content"></p>

<!-- 输入 p#text1 -->
<p id="text1"></p>
```

自动写入属性，例如输入`img[src=example.jpg]`

```html
<img src="example.jpg" alt="">
```

自动补全内容，使用`{}`。例如输入`p{text}`

```html
<p>text</p>
```

组合补全，使用`()`和`+`，例如输入`p>((ul#name>li*3)+(ul#address>li*3))`

```html
<p>
    <ul id="name">
        <li></li>
        <li></li>
        <li></li>
    </ul>
    <ul id="address">
        <li></li>
        <li></li>
        <li></li>
    </ul>
</p>
```