Django 安装

```bash
pip install django
# 通过pip下载

sudo apt install python3-django -y
# 通过apt安装django
```

创建项目

```bash
django-admin startproject <project_name>
# 创建项目
```



目录

DjangoProject
├── DjangoProject
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py	  # 程序的配置文件
│   ├── urls.py		 # 程序的路由系统，即url和处理其函数对应的关系
│   └── wsgi.py		# 指定框架的wsgi
└── manage.py	   # 管理程序的文件，启动和结束

修改 settings.py 中`ALLOWED_HOSTS[]` 填写主机地址



```bash
django-admin startapp <app_name>
# 创建项目下的app
```

app01
├── admin.py		# 数据库后台
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py		# 数据库操作
├── tests.py		  # 单元测试
└── views.py		# 业务逻辑代码



1. 设置路由
2. 在app中写好url对应函数
   1. 处理数据
   2. 通过HttpResponse 方法返回

```bash
python3 manage.py runserver 0.0.0.0:8000
# 启动程序并监听广播IP，8000端口
```



如果需要分开html前端代码与后端，可以调用render 方法

```python
def login_view(request):
    return render(request, 'form.html')
```



app数据库（model）模型同步到服务器数据库

首先将Django的MySQLDB换成pymysql，在项目下`__init__.py`

```python
import pymysql

pymysql.install_as_MySQLdb()
```



在setting中设置数据库

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_learning',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 3306
    }
}
```



生成同步文件并同步

```bash
python3 manage.py makemigrations
# Create migration files
python3 manage.py migrate
# Migrate
```

