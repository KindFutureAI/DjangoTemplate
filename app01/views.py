from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.viewsets import ModelViewSet
from app01.models import UserInfo
from app01.serializer import UserInfoSerializer
from app01.filter import UserInfoFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserInfoViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    filter_class = UserInfoFilter
    filter_fields = ['username',]
    search_fields = ('username',)





# Create your views here.

def index(request):
    return render(request, 'index.html')







# @login_required  # 确保用户必须登录才能访问视图
# def my_view(request):
#     pass
#
#
#
#
# @permission_required('myapp.add_post')  # 确保用户必须具有 myapp 应用程序中 Post 模型的 add 权限才能访问视图
# def my_view(request):
#     pass