# HTML

## 文字样式

| 标记                    | 显示效果       |
| --------------------- | ---------- |
| `<b></b>`             | <b>加粗</b>  |
| `<i></i>`             | <i>斜体</i>  |
| `<u></u>`             | <u>下划线</u> |
| `<s></s>`             | 删除线        |
| `<big></big>`         | 放大         |
| `<small></small>`     | 缩小         |
| `<strong></strong>`   | 加强         |
| `<em></em>`           | 强调         |
| `<address></address>` | 显示网址       |
| `<code></code>`       | 代码块        |

## 表单

`form`标签用于将表单包括进来，其属性有`action`, `method`即动作与提交方式

```html
<form action="example.php" method="post">
    <table>
        <tr>
            <td>Username</td>
            <td><input type="text" name="username"></td>
        </tr>
        <tr>
            <td>Password</td>
            <td><input type="password" name="password"></td>
        </tr>
        <tr>
            <td><input type="submit" value="submit"></td>
        </tr>
    </table>
</form>
```

此代码在点击submit按钮之后，会将username和password以post方式发送至服务器脚本example.php，并以POST中的数组储存，即`$_POST['username']`和`$_POST['password']`。

