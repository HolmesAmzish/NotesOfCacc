```python
if __name__ == "__main__":
    app.run(host="localhost", debug=True, threaded=True)
```



## 路由

使用 `route()` 装饰器来把函数绑定到URL

@app.route修饰器

```python
@app.route("/")
def index():
    return "index page"

@app.route('/hello')
def hello():
    return 'Hello, World'
```



### 变量规则

```python
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {subpath}'
```

### URL 构建

### HTTP 方法

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```



## 渲染模板

`render_template()` 方法可以渲染模板

```python
from flask import render_template

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

## Base64 编码

Base64编码是一种将二进制数据（如文件、图片或其他非文本数据）转化为可打印的ASCII字符的编码方法。它通过将每三字节（24位）的数据拆分为四个六位的块来表示，结果是一个由字母、数字和符号组成的字符串，通常用于在需要文本格式传输的地方（如电子邮件或HTTP协议）传输二进制数据。

具体来说，Base64编码有以下几个关键特点：

1. **编码过程**：

   - 每三个字节的输入数据（24位）被分成四个6位的部分。
   - 每个6位的部分映射到Base64字符集中的一个字符。
   - 如果输入的数据长度不是3的倍数，编码结果会用`=`符号填充，以确保输出的长度是4的倍数。

2. **Base64字符集**： Base64编码使用一个包含64个字符的字符集：

   ```
   A-Z, a-z, 0-9, +, /
   ```

   在URL和文件名中使用时，一些字符（如`+`和`/`）可能会被替换为URL安全字符（如`-`和`_`），以避免冲突。

3. **常见用途**：

   - 电子邮件：邮件内容通常使用Base64编码来处理二进制附件。
   - 数据传输：当需要通过JSON、XML等文本格式传输二进制数据时，常常使用Base64编码。
   - Web开发：例如，将图片编码为Base64格式嵌入到HTML或CSS文件中。

例如，将字符串`hello`编码成Base64后是：`aGVsbG8=`

它的解码过程将Base64字符串转换回原始的二进制数据或文本。

你有遇到具体的Base64编码使用场景吗？
