# Tailwind CSS Cheatsheet

## 1. 布局 Layout

| 功能      | 类名示例                                                     | 说明                       |
| --------- | ------------------------------------------------------------ | -------------------------- |
| 显示      | `block`、`inline`、`inline-block`、`flex`、`grid`            | 控制元素显示方式           |
| Flex 布局 | `flex-row` (默认)  `flex-col`  `flex-wrap`  `items-center`  `justify-between` | Flex方向、换行、对齐方式   |
| Grid 布局 | `grid`  `grid-cols-3`  `grid-rows-2`  `gap-4`                | 网格列数、行数、间隙       |
| 宽高      | `w-32`  `h-16`  `w-full`  `h-screen`                         | 固定宽高、百分比、屏幕高度 |
| 最大宽度  | `max-w-sm`  `max-w-full`                                     | 最大宽度                   |
| 最小宽度  | `min-w-0`  `min-w-full`                                      | 最小宽度                   |
| 定位      | `relative`  `absolute`  `fixed`  `top-0`  `left-1/2`         | 绝对/相对定位              |
| 溢出处理  | `overflow-auto`  `overflow-hidden`                           | 控制溢出行为               |
| 层级      | `z-10`  `z-50`                                               | z-index                    |

------

## 2. 间距 Spacing

| 功能           | 类名示例                 | 说明                      |
| -------------- | ------------------------ | ------------------------- |
| 外边距 margin  | `m-4`  `mt-2`  `mx-auto` | 四边统一，或分别上下/左右 |
| 内边距 padding | `p-6`  `py-3`  `px-2`    | 四边统一，或分别上下/左右 |
| 间距           | `space-x-4`  `space-y-2` | 横向/纵向子元素间距       |
| 负间距         | `-m-1`  `-mt-2`          | 负外边距                  |

------

## 3. 排版 Typography

| 功能     | 类名示例                                         | 说明                     |
| -------- | ------------------------------------------------ | ------------------------ |
| 字体大小 | `text-xs`  `text-sm`  `text-lg`  `text-2xl`      | 从超小到较大字体         |
| 字体颜色 | `text-gray-700`  `text-red-500`  `text-white`    | 颜色                     |
| 字体粗细 | `font-thin`  `font-normal`  `font-bold`          | 细体、普通、加粗         |
| 行高     | `leading-none`  `leading-tight`  `leading-loose` | 控制行间距               |
| 字体样式 | `italic`  `not-italic`                           | 斜体/正常                |
| 文本对齐 | `text-left`  `text-center`  `text-right`         | 左中右对齐               |
| 文本溢出 | `truncate`  `overflow-ellipsis`                  | 文本截断省略号           |
| 文本装饰 | `underline`  `line-through`                      | 下划线，删除线           |
| 字体族   | `font-sans`  `font-serif`  `font-mono`           | 无衬线、有衬线、等宽字体 |

------

## 4. 背景 Background

| 功能       | 类名示例                                            | 说明                   |
| ---------- | --------------------------------------------------- | ---------------------- |
| 背景色     | `bg-white`  `bg-gray-200`  `bg-blue-500`            | 背景颜色               |
| 背景透明度 | `bg-opacity-50`                                     | 透明度50%              |
| 背景图片   | `bg-cover`  `bg-center`  `bg-no-repeat`             | 图片大小、位置、不重复 |
| 渐变背景   | `bg-gradient-to-r`  `from-blue-400`  `to-green-500` | 线性渐变               |

------

## 5. 边框 Borders

| 功能     | 类名示例                                         | 说明             |
| -------- | ------------------------------------------------ | ---------------- |
| 边框宽度 | `border` (1px)  `border-2`  `border-t-4`         | 全部或指定边宽度 |
| 边框颜色 | `border-gray-300`  `border-red-500`              | 边框颜色         |
| 圆角     | `rounded`  `rounded-lg`  `rounded-full`          | 圆角大小         |
| 边框样式 | `border-dashed`  `border-dotted`  `border-solid` | 边框样式         |

------

## 6. 交互与状态 States

| 功能 | 类名示例                                | 说明           |
| ---- | --------------------------------------- | -------------- |
| 悬停 | `hover:bg-blue-500`  `hover:text-white` | 鼠标悬停时样式 |
| 聚焦 | `focus:outline-none`  `focus:ring-2`    | 聚焦时样式     |
| 激活 | `active:bg-blue-700`                    | 激活状态       |
| 禁用 | `disabled:opacity-50`                   | 禁用时透明度   |

------

## 7. 显示与可见性

| 功能      | 类名示例                                 | 说明         |
| --------- | ---------------------------------------- | ------------ |
| 显示/隐藏 | `hidden`  `block`  `inline-block`        | 显示与隐藏   |
| 透明度    | `opacity-100`  `opacity-50`  `opacity-0` | 不透明度     |
| 可见性    | `visible`  `invisible`                   | 元素是否可见 |

------

## 8. 其他常用 Utilities

| 功能         | 类名示例                                    | 说明               |
| ------------ | ------------------------------------------- | ------------------ |
| 阴影         | `shadow`  `shadow-lg`  `shadow-none`        | 元素阴影           |
| 光环（ring） | `ring`  `ring-2`  `ring-blue-500`           | 聚焦和辅助环       |
| 文字换行     | `break-words`  `truncate`                   | 控制文字换行和截断 |
| 过渡动画     | `transition`  `duration-300`  `ease-in-out` | 过渡效果及持续时间 |
| 游标         | `cursor-pointer`  `cursor-default`          | 鼠标样式           |

------

## 9. 响应式设计（Breakpoints）

| 前缀   | 说明     |
| ------ | -------- |
| `sm:`  | ≥ 640px  |
| `md:`  | ≥ 768px  |
| `lg:`  | ≥ 1024px |
| `xl:`  | ≥ 1280px |
| `2xl:` | ≥ 1536px |

**用法示例：**

```html
<div class="text-base md:text-lg lg:text-xl">
  响应式文字大小
</div>
```

------

## 10. 暗黑模式（Dark Mode）

- 在配置文件中启用 `darkMode: 'class'` 后：

```html
<div class="bg-white dark:bg-gray-900 text-black dark:text-white">
  白天背景白色，晚上背景深灰色
</div>
```