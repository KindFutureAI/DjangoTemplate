"""
URL configuration for django_practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("pwd_manage/", include("app01.urls")),
    path("api/v1/", include("app01.urls"))  # 相当于蓝图, 而且 这里的api/vi/ 这最有一个/ 一定要有
]

"""
在 Django 项目中，include 函数用于将 URL 模式委托给其他 URL 模块处理。具体来说：
include 函数通常用于将 URL 模式分解到不同的应用中，使得每个应用可以管理自己的 URL 配置。
在 urlpatterns 列表中，path("pwd_manage/", include("app01.urls")) 这一行表示：
当请求的 URL 以 pwd_manage/ 开头时，Django 会将剩余的部分传递给 app01 应用中的 urls.py 文件进行进一步处理。
这样可以保持项目的 URL 配置模块化和可维护性。
例如，如果请求的 URL 是 http://example.com/pwd_manage/user/123/，Django 会将 user/123/ 传递给 app01 应用的 urls.py 文件进行处理。
"""