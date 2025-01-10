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

