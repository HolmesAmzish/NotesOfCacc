# CSS选择器

## CSS基本选择器

CSS有几种不同类型的选择器，基本选择器有标记选择器，类别选择器和ID选择器三种

### 标记选择器

通过声明标记采用指定的CSS样式

```html
<html>
 <style>
     h1{
         color: red;
         font-size: 25px;
     }
 </style>
</html>
```

### 类别选择器

类别选择器的名称可以由用户自定义，属性和值跟标记选择器一样，也必须符合CSS规范

```html
<html>
<head>
    <title>Class Selector</title>
    <style type="text/css">
        .red{
            color: red;
            font-size: 18px;
        }
        .green{
            color: green;
            font-size: 20px;
        }
    </style>
</head>

<body>
    <p class="red">Class = red</p>
    <p class="green">Class = green</p>
</body>
</html>
```

类别选择器的属性优先级大于标记选择器，当本标签被声明为某类时，会优先显示类别选择器所定义的属性。标签选择器和类别选择器可以进行组合，形成交集选择器。

### ID选择器

```html
<html>
 <head>
     <title>ID selector</title>
     <style type="text/css">
         #bold{
             font-weight: blod;
         }
         #green{
             font-size:30px;
             color: #009900;
         }
     </style>
 </head>
 <body>
     <p id="bold">
         ID 选择器1
     </p>
     <p id="green">
         ID 选择器2
     </p>
 </body>
</html>
```

ID选择器可以用于多个标签，但是一个标签不可以被定义多个ID，因为JavaScript等其他脚本语言同样可以调用id。如果一个HTML中有两个相同的id标记，会导致JavaScript在查找id时出错，例如`getElementById()`。而因为JavaScript也能调用HTML中设置的id，因此最好一个id仅赋予一个HTML标记。

### 交并集选择器

交集选择器由两个选择器连接构成，其结果时选中两者中各自元素范围的交集。其中一个必须是标记选择器，第二个必须是类别选择器或者ID选择器。例如`h3.class1 {color: red; font-size: 23px;}`，就定义了一个类别为class1的h3标签。

并集选择器成为集体申明，可以将多个标签选择器，类别选择器等一同进行CSS修饰。

```css
h1, h2, p{
    color: purple;
    font-size: 15px;
}
```

### 后代选择器

在CSS选择器中，可以通过嵌套的方式对特殊位置的HTML标签进行声明，例如在一个`<p></p>`标签内嵌套了一个`<span></span>`，则可以使用后代选择器进行相应的控制。

```css
p span{
    color: red;
}
span{
    color: blue;
}
```

```html
<p><span>The content here will be red</span></p>
<span>The content here will be blud</span>
```

### *基本选择器表*

| 选择器                  | 类型    | 功能描述                              |
| -------------------- | ----- | --------------------------------- |
| *                    | 通配选择器 | 选择文档中所有的HTML元素                    |
| E                    | 元素选择器 | 选择指定类型的HTML元素                     |
| #id                  | ID选择器 | 选择指定ID属性值为"id"的任意类型元素             |
| .class               | 类别选择器 | 选择指定class属性值为"class"的任意类型的任意多个元素  |
| .class1.class2       | 交集选择器 | 选择class属性中同时有"class1"和"class2"的元素 |
| selector1, selector2 | 并集选择器 | 将每一个选择器匹配的元素合并                    |

## 在HTML使用CSS的方法

### 内行样式

直接修改HTML标签的属性来使用CSS进行修饰

```html
<p style="color:#FF0000; font-size:20px;">
    Content text.
</p>
```

### 内嵌式

直接在HTML中head标签之间，打开style标签进行修饰。

### 连接式

创建一个独立的CSS文件，使得HTML代码与CSS代码分离，使得前期预制和后期维护更加方便

```css
/* 创建一个CSS文件 */
h2{
    color: #0000FF;
}
p{
    color: #FF0000;
    text-decoration: underline;
    font-weight: bold;
    font-size: 15px;
}
```

```html
<html>
    <head>
        <title>CSS Stylesheet</title>
        <link href="filename.css" type="text/css" rel="stylesheet">
    </head>
</html>
```

### 导入样式

导入样式与连接式的功能基本相同，只是在语法和运作方式上略有区别。采用import方式导入样式表，在初始化HTML之前，回到如到HTML结构中，作为文件的一部分。

```html
@import url(sheet.css);
@import url('sheet.css');
@import url("sheet.css");
@import sheet.css;
@import "sheet.css";
@import 'sheet.css';
```

## CSS的继承和层叠特性

### 继承关系

所有的CSS语句都是基于各个标记之间的继承关系，如果将各个HTML标记看作一个容器，其中被包含的容器会继承他的容器的风格样式。子标记会继承父标记的样式风格，并且可以在父标记的样式风格上进行修改，产生新的样式，而子标记的风格样式完全不会影响父标记。例如如下代码

```html
<html>
<head>
    <title>继承关系演示</title>
    <style>
        h1{
            color:blue;                    /* 颜色 */
            text-decoration:underline;    /* 下划线 */
        }
        em{
            color:red;                    /* 颜色 */
        }
        li{
            font-weight:bold;
        }
    </style>
</head>
<body>
    <h1>前端<em>Web</em>技术</h1>
    <ul>
        <li>Web设计与开发需要使用以下技术：
            <ul>
                <li>HTML</li>
                <li>CSS
                <ul>
                    <li>选择器</li>
                    <li>在HTML使用CSS的方法</li>
                    <li>CSS的继承和层叠特性</li>                
                </ul>
                </li>
                <li>Javascript</li>
            </ul>
        </li>
        <li>各种其他所需工具
            <ol>
                <li>Flash</li>
                <li>Dreamweaver</li>
                <li>Photoshop</li>
            </ol>
        </li>
    </ul>
    <p>如果您有任何问题，欢迎联系我们</p>
</body>
</html>
```

Web作为`<em></em>`标记的内容嵌套于`<h1></h1>`中，所以在在其基础上添加了红色且下划线的属性。同时由于`color`的样式冲突，按照其优先级，红色覆盖掉了标题的蓝色。

### 层叠特性

层叠指样式的优先级，CSS样式在针对同意元素配置同一属性时，会依据层叠规则也就是权重或者优先级来处理冲突。选择应用权重高的CSS选择器所指定的属性，一般也被描述为权重高的属性覆盖权重低的属性，因此被称为层叠。优先级的规则可以表述为：**行内样式 > ID样式 > 类别样式 > 标记样式**

## 关系选择器

| 选择器 | 类型       | 功能描述                         |
| --- | -------- | ---------------------------- |
| E F | 后代选择器    | 选择匹配的F元素，且匹配的F元素被包含在匹配的E元素内  |
| E>F | 子元素选择器   | 选择匹配的F元素，且匹配的F元素时所匹配的E元素的子元素 |
| E+F | 相邻兄弟选择器  | 选择匹配的F元素，且匹配的F元素紧位于匹配的E元素的后面 |
| E-F | 相邻兄弟组选择器 | 选择匹配的F元素，且匹配的F元素位于匹配的E元素的后面  |

## 属性选择器

| 选择器                 | 功能描述                       |
| ------------------- | -------------------------- |
| [attribute]         | 用于选取带有指定属性的元素              |
| [attribute=value]   | 用于选取带有指定属性以及指定值的元素         |
| [attribute*=value]  | 用于选取属性值中包含指定值的元素           |
| [attribute~=value]  | 用于选取属性值中包含指定值，且指定值是完整单词的元素 |
| [attribute^=value]  | 用于选取属性值以指定值开头的元素           |
| [attribute\|=value] | 用于选取属性值以指定值开头，且该值是完整单词的元素  |
| [attribute$=value]  | 匹配属性值以指定值为结尾的每个元素          |

# 盒子模型

- margin 清除边框外的区域，外边距是透明。
- border 围绕在内边距和内容外的边框。
- padding 清除内容周围的区域，内边距是透明的。
- content 合资的内容，显示文本和图像

![box](../../img/17.gif)
