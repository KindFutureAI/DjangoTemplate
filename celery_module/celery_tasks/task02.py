#task02
import time
from celery_module.celery_tasks.celery_app import cel
@cel.task
def send_msg(name):
    time.sleep(5)
    return "完成向%s发送短信任务"%name
