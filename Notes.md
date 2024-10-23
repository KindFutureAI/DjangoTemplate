
# 1 创建和开发web 
**安装**
```bash
pip install django

pip show django  # 看版本
```

## **1 创建项目（通过命令行)

```bash
django-admin startproject 自定义的项目名称
```
创建完成后，可以看到创建了很多文件，这些都是django项目的必备文件。这里简单放上，官方的解释

最外层的 mysite/ 根目录只是你项目的容器， 根目录名称对 Django 没有影响，你可以将它重命名为任何你喜欢的名称。
	manage.py: 一个让你用各种方式管理 Django 项目的命令行工具。你可以阅读 django-admin 和 manage.py 获取所有 manage.py 的细节。
	里面一层的 mysite/ 目录包含你的项目，它是一个纯 Python 包。它的名字就是当你引用它内部任何东西时需要用到的 Python 包名。 (比如 mysite.urls).
	mysite/init.py：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。如果你是 Python 初学者，阅读官方文档中的 更多关于包的知识。
	mysite/settings.py：Django 项目的配置文件。如果你想知道这个文件是如何工作的，请查看 Django 配置 了解细节。
	mysite/urls.py：Django 项目的 URL 声明，就像你网站的“目录”。阅读 URL调度器 文档来获取更多关于 URL 的内容。
	mysite/asgi.py：作为你的项目的运行在 ASGI 兼容的 Web 服务器上的入口。阅读 如何使用 ASGI 来部署 了解更多细节。
	mysite/wsgi.py：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。阅读 如何使用 WSGI 进行部署 了解更多细节。 

## 2 测试运行情况
项目的根目录下，打开终端，运行

```
python manage.py runserver localhost:8000
```

然后打开浏览器，输入网址, 会看到初始界面：

```
http://127.0.0.1:8000/admin

# 官方文档：https://docs.djangoproject.com/zh-hans/
```

## 3 创建app应用
打开终端执行

```
python manage.py startapp app01

补充删除app的方式：
manage.py migrate my_app_name zero 
```

## 4. 注册app

如果是使用pycharm，按照我截图方式创建的项目，则忽略这一步，因为已经注册好了。  
在项目的setting.py文件中，找到INSTALLED_APPS节点，新增注册语句即可完成注册：

```
'app01.apps.App01Config'
```

特别注意：如果不注册app，那么app下的模型model.py文件中的模型类，是无法创建数据表的。
```
# django_practice/settings.py


# Application definition  
  
INSTALLED_APPS = [  
    "django.contrib.admin",  
    "django.contrib.auth",  
    "django.contrib.contenttypes",  
    "django.contrib.sessions",  
    "django.contrib.messages",  
    "django.contrib.staticfiles",  
    "app01.apps.App01Config"    # 这里
]
```

## 5 配置数据库等等
打开`setting.py`，找到配置数据库的地方。我这里使用的是sqlite3数据库。如果想要使用别的数据库，可以去官方文档搜索相应的引擎配置。

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

默认的路径是在项目的根目录下的，如果有需求，可以改到别的任何地方。

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'D:/Databases/personinfo/person.sqlite3',
    }
}
```


### 其他配置（可有可无）

打开`setting.py`  
**5.1 设置语言为中文，设置时区为上海**

```
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
```

否则可能出现中文乱码。时区一定要改，否则如果开发项目时候使用了django的获取时间API，获取的是美国时区，会比中国慢。  
** 设置关闭网页时，结束所有会话**

```
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
```

**5.3 设置静态文件夹位置**  
当需要访问静态文件时，会根据设置的文件夹去寻找

```
STATICFILES_DIRS = [
    BASE_DIR / "static",  # 假设你的静态文件在项目的static文件夹中
]
```


## 6 编写url和视图函数对应关系（url.py文件）

##### 6.1 配置项目url

目前尾汁，可以在项目名称里找到一个`urls.py`文件，打开后内容如下。这就是我们之前的访问的admin路径配置

```
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
]
```

修改如下：

```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("PasswordManage/", include("PwdMgeapp.urls")),
]
```

几个注意的点：

- `PasswordManage`可以改为你想要的路径
- `PwdMgeapp`必须与你的应用名称相同
- 强烈推荐使用`include`包含，这样可以防止项目有多个应用时，路径重名问题。

##### 6.2 设置应用url

在应用程序文件夹（PwdMgeapp）下，创建`urls.py`，添加内容

```
from django.urls import path
from . import views
urlpatterns = [
    path("index/", views.index, name="index"),
]
```

##### 6.3 编写视图函数

pycharm里找到左下方的django结构，在app下右键视图，指向“New View”，点击“View Function” 快捷创建视图，修改视图函数名为【index】，这里需要与6.2里设置的path名对应。  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/da17c075b45636cd4c8608e37c0778eb.png)  
修改index视图函数如下：

```
def index(request):
    return render(request, "index.html")
```

如果没有使用pycharm，那么在【应用名】的文件夹下，找到“views.py”，打开后，把上面的视图函数直接复制进去就可以了。

##### 6.4 编写html文件

在`templates`文件夹下新建`index.html`，需要与6.3视图函数中render里的参数对应。内容如下：

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
welcome django
</body>
</html>
```

`templates`里存放各种html文件，在与`templates`同目录下，创建一个`static`文件夹，用来存储静态文件，如图片、css、js等等。

##### 6.5 运行程序

点击pycharm的绿色三角形运行程序，或者命令行输入

```
python manage.py runserver
```

启动成功后，访问下面网址

```
http://127.0.0.1:8000/PasswordManage/index/
```

发现显示内容  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/55d039e262993de891c1e6b5043f5b1e.png)  
到此就运行成功。


# 2 搭建后台应用

### 1 运行项目：检查初始状态是否正常

```bash
python manage.py runserver
```

#### 1.4 配置mysql数据库

```bash
 
DATABASES = {  
    "default": {  
        # "ENGINE": "django.db.backends.sqlite3",  
        # "NAME": BASE_DIR / "db.sqlite3",  
        # choose mysql        "ENGINE": "django.db.backends.mysql",  
        "NAME": "django_practice",  
        "USER": "root",  
        "PASSWORD": "xxxxxx",  
        "HOST": "localhost",  
        "PORT": "3306",  
    }  
}
```

在项目django_practice项目下的init.py中加入如下代码

```bash
pip install pymysql
```

```bash
import pymysql
pymysql.version_info = (1, 4, 3, "final", 0)
pymysql.install_as_MySQLdb()
```

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/aba47b80f0d19ae44be0845a215b57f0.png)

#### 1.5 创建数据库类

在django_practice的model.py中加入如下代码
```bash
from django.db import models


class UserInfo(models.Model):
    username = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=128)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.username
```

执行如下命令创建数据库

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 1.6 使用Django后台进行数据管理

在django_practice应用目录下加入如下代码

```bash
from django.contrib import admin
from django_practice.models import UserInfo

admin.site.site_header = '任务管理系统'


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password',)
    list_display_links = ('username',)
    list_per_page = 50


admin.site.register(UserInfo, UserInfoAdmin)
```

创建后台管理员用户

```bash
python manage.py createsuperuser
```
![[Pasted image 20241023220459.png]]
 

### 2、Django rest framework配置

```bash
pip install djangorestframework
# 暂时不装也可以
pip install markdown
# 用于数据筛选
pip install django-filter
```

在settings中注册framework

```bash
INSTALLED_APPS = [
    'rest_framework',
    'django_filters',
]
```

#### 2.1 序列化
  
在app目录下创建serializer.py，添加如下代码

```bash
from django_practice.models import UserInfo
from rest_framework import serializers


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
```

#### 2.2 添加视图

在app目录下的view.py中加入如下代码：

```bash
from rest_framework.viewsets import ModelViewSet
from django_practice.models import UserInfo
from django_practice.serializer import UserInfoSerializer
from django_practice.filter import UserInfoFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserInfoViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    filter_class = UserInfoFilter
    filter_fields = ['username',]
    search_fields = ('username',)
```

#### 2.3 添加路由

在app目录下创建urls.py文件：

```bash
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django_practice.views import UserInfoViewSet

router = DefaultRouter()
router.register('UserInfo', UserInfoViewSet, basename='UserInfo')

urlpatterns = [
]

urlpatterns += [
    path('', include(router.urls)),
]
```

#### 2.4 在项目根目录下的urls中加入如下代码

```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('django_practice.urls')),
]
```

#### 2.5 api测试

`http://127.0.0.1:8000/api/v1/UserInfo/`

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/f4e9405f6630fc5cad9ff4cf435d4838.png)

#### 2.6 筛选和搜索功能配置

在app根目录下创建filter.py文件

```bash
from django_filters import FilterSet, filters
from django_practice.models import UserInfo


class UserInfoFilter(FilterSet):
    name = filters.CharFilter(field_name='username', lookup_expr='icontains')

    class Meta:
        model = UserInfo
        fields = ('username',)
```

修改app目录下的view文件：`在这里插入代码片`

```bash
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from django_practice.models import UserInfo
from django_practice.serializer import UserInfoSerializer
from django_practice.filter import UserInfoFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserInfoViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    filter_class = UserInfoFilter
    filter_fields = ['username']
    search_fields = ('username',)
```

在settings中注册django_filters：

```bash
INSTALLED_APPS = [
    'django_filters',
]

# REST_FRAMEWORK增加全局过滤配置  
REST_FRAMEWORK = {  
 'DEFAULT_FILTER_BACKENDS': [  
     'django_filters.rest_framework.DjangoFilterBackend',
     'rest_framework.filters.SearchFilter',
 ],  
}
# 如果可以实现模糊查询，则以下语句可省略
FILTERS_DEFAULT_LOOKUP_EXPR = 'icontains'
```

Django Rest Framework页面出现Filters图标说明配置成功

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/7201653d71e8099f38c48453ba5c4093.png)

####  2.7 分页设置

在settings.py中做如下修改

```bash
# REST_FRAMEWORK增加全局过滤配置  
REST_FRAMEWORK = {  
    # 设置分页  
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  
    'PAGE_SIZE': 10,
}
```

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/afe78ad5d2a3b13acec42fd2315500bc.png)  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/709286a0c2f4d0fc166f47dde2b606f2.png)

##### 3、自动生成api文档

```bash
pip install drf-yasg
```

在项目文件夹urls.py中做如下修改

```bash
INSTALLED_APPS = [
    'drf_yasg',  # swagger
]
```

在app的urls.py中做如下修改

```bash
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API平台",
        default_version="v1",
        description="接口文档",
        terms_of_service="",
        contact=openapi.Contact(email='2495128088@qq.com'),
        license=openapi.License(name="BSD License"),
    ),
    public=True
)

router = DefaultRouter()
router.register('UserInfo', UserInfoViewSet, basename='UserInfo')

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
]
```

文档查看文档是否成功，`http://127.0.0.1:8000/api/v1/docs/`

![[Pasted image 20241023220554.png]]





















# 常见的问题
### 1 django 中已经定义好了表，但是ORM迁移没在mysql中创建成功

解决方法
```bash
# 1 删除现有的迁移文件，重新生成新的迁移文件：
   rm app01/migrations/0001_initial.py
   python manage.py makemigrations app01

# 2 强制应用迁移 
有时候，Django 可能会认为某些迁移已经应用过，但实际上并没有。你可以尝试强制应用迁移：
   python manage.py migrate --fake app01 zero
   python manage.py migrate app01

# 3 检查数据库表 
确保 app01_userinfo 表已经创建：
   USE django_practice;
   SHOW TABLES LIKE 'app01_userinfo';
# 结果：找到了！ 成功了！

mysql> SHOW TABLES LIKE 'app01_userinfo';
+--------------------------------------------+
| Tables_in_django_practice (app01_userinfo) |
+--------------------------------------------+
| app01_userinfo                             |
+--------------------------------------------+
1 row in set (0.00 sec)

```