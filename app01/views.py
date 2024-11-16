from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.viewsets import ModelViewSet
from app01.models import UserInfo
from app01.serializer import UserInfoSerializer
from app01.filter import UserInfoFilter
from django_filters.rest_framework import DjangoFilterBackend

from mycelery.sms.tasks import send_sms, send_sms2
from datetime import datetime, timedelta


class UserInfoViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    filter_class = UserInfoFilter
    filter_fields = ['username',]
    search_fields = ('username',)





# Create your views here.

def index(request):
    return render(request, 'index.html')


def celery_sms(request):
        ################################# 异步任务

    # 1. 声明一个和celery一模一样的任务函数，但是我们可以导包来解决

    res1 = send_sms.delay("110")
    res2 = send_sms2.delay("119")
    # send_sms.delay()  # 如果调用的任务函数没有参数，则不需要填写任何内容
    print(f"res1: {res1}")
    print(f"res2: {res2}")

    ################################# 定时任务

    ctime = datetime.now()
    # 默认用utc时间
    utc_ctime = datetime.fromtimestamp(ctime.timestamp())
    time_delay = timedelta(seconds=10)
    task_time = utc_ctime + time_delay
    res3 = send_sms.apply_async(["911", ], eta=task_time)  # eta: ETA，即执行时间
    print(f"res3.id: {res3.id}")


    return HttpResponse('ok') 
 
def room(request, group_num):
    return render(request, 'socket_index.html', {
        "group_num": group_num
        })