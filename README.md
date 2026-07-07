# python

#### [1、python教程](https://liaoxuefeng.com/books/python/introduction/index.html) : liaoxuefeng blog

```
# virtualenv的安装
pip install virtualenv

# 创建虚拟环境
virtualenv venv1

# 激活虚拟环境
.\venv1\Scripts\Activate.ps1

# PyCharm创建Django项目：勾选使用Virtualenv创建虚拟环境

------------------------------------------------------------------

# 安装django
pip install django
pip install django==3.1.6 # 安装指定版本

# 创建项目
django-admin startproject mysite

mysite/ # 根目录
    manage.py # Django命令行工具
    mysite/ # 项目配置目录
        __init__.py # 空文件，告诉python这个目录是python包
        settings.py # 项目配置文件
        urls.py # 项目所有urls声明汇总
        asgi.py # ASGI服务器的入口文件
        wsgi.py # WSGI服务器的入口文件

# 启动项目
python manage.py runserver

# 创建应用
python manage.py startapp demo

# 注册app到settings.py
mysite\settings.py
INSTALLED_APPS = [
    'demo',
]

# mysite/urls.py 加入app对应urls
urlpatterns = [
    path('', include('demo.urls')),
]

# 编写视图函数和 URL 配置
demo\views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the demo index.")

# demo\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]   

------------------------------------------------------------------

# 新建app并注册
python manage.py startapp tasks
mysite\settings.py
mysite\urls.py

# 创建模型(M)
tasks\models.py
# 生成数据库迁移文件
python manage.py makemigrations
# 应用数据库迁移文件
python manage.py migrate

# 编写视图并配置路由URL(V)
tasks\views.py
tasks\urls.py

# 编辑模板(T)
tasks\templates\tasks\index.html

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# 创建超级用户
python manage.py createsuperuser
```
// Python交互模式
C:\Users\W000709> python
│Python 3.x ... on win32                                  │
│Type "help", ... for more information.                   │
│>>> exit() 
```

```
// Python脚本模式
C:\Users\W000709> python 43.helloword.py
```

```
// 切换盘符
C:\Users\W000709> D:
D:\>
```