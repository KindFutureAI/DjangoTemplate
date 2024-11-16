# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# 设置默认的 Django 设置模块 TODO
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

app = Celery('your_project')

# 使用 Django 的设置文件中的 CELERY_ 前缀的设置 TODO
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动发现并注册任务
app.autodiscover_tasks()