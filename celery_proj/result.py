from celery.result import AsyncResult
from celery_task import cel

'''
AsyncResult 详解：
1. AsyncResult(id, app=None)
   id: 任务id
   app: celery实例对象
2. status: 任务状态
   1. PENDING: 等待执行
   2. STARTED: 正在运行
   3. RETRY: 正在重试
   4. FAILURE: 失败
   5. SUCCESS: 成功
3. get(): 获取任务结果
  1. get(timeout=None, propagate=True)  # 获取任务结果，如果任务没有执行完成，那么就一直阻塞，直到任务执行完成。
  2. get(timeout=None, propagate=False)  # propagate: 是否抛出异常，默认为True
  3. get(timeout=None, propagate=True, interval=0.1, interval_step=0.01)  # interval: 阻塞的时间间隔，默认是0.1秒
  4. get(timeout=None, propagate=False, interval=0.1, interval_step=0.01)  # interval_step: 阻塞时间间隔的步长，默认是0.01秒
4. forget(): 删除任务结果
'''

async_result=AsyncResult(id="a4e5457-460b-406f-b2cc-4dee5d1db8b8", app=cel)

if async_result.successful():
    result = async_result.get()
    print("任务执行完成", result)
    # result.forget() # 将结果删除

elif async_result.failed():
    print('执行失败')

elif async_result.status == 'PENDING':
    print('任务等待中被执行')

elif async_result.status == 'RETRY':
    print('任务异常后正在重试')

elif async_result.status == 'STARTED':
    print('任务已经开始被执行')
